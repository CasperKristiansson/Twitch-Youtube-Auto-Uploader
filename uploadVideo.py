from __future__ import unicode_literals
import youtube_dl
import requests
import os
import shutil
import time

import argparse
import http.client
import httplib2
import random
import time
from videoDetails import Video

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

def delete():
  folder = 'Video'
  for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
      if os.path.isfile(file_path) or os.path.islink(file_path):
        os.unlink(file_path)
      elif os.path.isdir(file_path):
        shutil.rmtree(file_path)
    except Exception as e:
      print('Failed to delete %s. Reason: %s' % (file_path, e))

def get_files():
  twitchClipLinks = []

  with open('apiTwitchClipLinks.txt', 'r') as filehandle:
    for line in filehandle:
      currentPlace = line[:-1]
      twitchClipLinks.append(currentPlace)

  return twitchClipLinks

def current_file():
  currentFile = []
  currentFileLength = []
  nextFile = []

  with open('currentFile.txt', 'r') as filehandle:
    for line in filehandle:
      currentPlace = line[:-1]
      currentFile.append(currentPlace)

  currentFileLength = len(currentFile)
  i = 0
  while i < currentFileLength + 1:
    nextFile.insert(0,1)
    i += 1

  with open('currentFile.txt', 'w') as filehandle:
    for listitem in nextFile:
      filehandle.write('%s\n' % listitem)

  return currentFileLength

def download_video(twitchClipLinks, currentFileLength):
  x = twitchClipLinks[currentFileLength]
  ydl_opts = {}
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      ydl.download([x])

def manage_file():
  files = os.listdir(os.curdir)

  for file in files:
    if '.mp4' in file:
        os.rename(file, file.translate(str.maketrans('','','0123456789-')))

  files = os.listdir(os.curdir)
  for file in files:
    if '.mp' in file:
      newfile = file.replace('.mp', '.mp4')
      os.rename(file, newfile)
      shutil.move(newfile, 'Video')

class YoutubeUpload:
  def __init__(self):
    self.MAX_RETRIES = 10

    self.RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError, http.client.NotConnected,
      http.client.IncompleteRead, http.client.ImproperConnectionState,
      http.client.CannotSendRequest, http.client.CannotSendHeader,
      http.client.ResponseNotReady, http.client.BadStatusLine)

    self.RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

    self.CLIENT_SECRETS_FILE = 'client_secrets.json'

    self.SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
    self.API_SERVICE_NAME = 'youtube'
    self.API_VERSION = 'v3'

  def get_authenticated_service(self):
      credential_path = os.path.join('credentials.json')
      store = Storage(credential_path)
      credentials = store.get()
      if not credentials or credentials.invalid:
          flow = client.flow_from_clientsecrets(self.CLIENT_SECRETS_FILE, self.SCOPES)
          credentials = tools.run_flow(flow, store)
      return build(self.API_SERVICE_NAME, self.API_VERSION, credentials=credentials)

  def initialize_upload(self, youtube, options):
    tags = None
    if options.keywords:
      tags = options.keywords.split(',')

    body=dict(
      snippet=dict(
        title=options.getFileName("video").split(".", 1)[0],
        description=options.description,
        tags=tags,
        categoryId=options.category
      ),
      status=dict(
        privacyStatus=options.privacyStatus
      )
    )

    videoPath = "Video/{}".format(options.getFileName("video"))
    insert_request = youtube.videos().insert(
      part=','.join(body.keys()),
      body=body,
      media_body=MediaFileUpload(videoPath, chunksize=-1, resumable=True)
    )

    self.resumable_upload(insert_request, options)

  def resumable_upload(self, request, options):
    response = None
    error = None
    retry = 0
    while response == None:
      try:
        print('Uploading file...')
        status, response = request.next_chunk()
        if response is not None:
          if 'id' in response:
            print ('The video with the id {} was successfully uploaded!'.format(response['id']))

            options.insertThumbnail(youtube, response['id'])
          else:
            exit('The upload failed with an unexpected response: {}'.format(response))
      except HttpError as e:
        if e.resp.status in self.RETRIABLE_STATUS_CODES:
          error = 'A retriable HTTP error {} occurred:\n{}'.format((e.resp.status, e.content))
        else:
          raise
      except self.RETRIABLE_EXCEPTIONS as e:
        error = 'A retriable error occurred: {}'.format(e)

      if error is not None:
        print (error)
        retry += 1
        if retry > self.MAX_RETRIES:
          exit('No longer attempting to retry.')

        max_sleep = 2 ** retry
        sleep_seconds = random.random() * max_sleep
        print ('Sleeping {} seconds and then retrying...').format((sleep_seconds))
        time.sleep(sleep_seconds)

if __name__ == '__main__':
  delete()
  VIDEO_URL = get_files()
  CURRENT_VIDEO = current_file()
  download_video(VIDEO_URL, CURRENT_VIDEO)
  manage_file()

  youtubeUpload = YoutubeUpload()
  args = Video()
  youtube = youtubeUpload.get_authenticated_service()

  try:
    youtubeUpload.initialize_upload(youtube, args)
  except HttpError as e:
    print ('An HTTP error {}} occurred:\n{}').format((e.resp.status, e.content))
