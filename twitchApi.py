from __future__ import unicode_literals
import youtube_dl
import requests
import os
import shutil
import time
import sys

import argparse
import http.client
import httplib2
import random

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

displayNameTopChannel = []
displayNameLinkTopChannel = []
viewsTopChannel = []
clipCreatorNameTopChannel = []
clipCreatorLinkTopChannel = []
clipUploadTimeTopChannel = []
currentFileTopChannel = []

with open('currentFileTopChannel.py', 'w') as filehandle:
    for listitem in currentFileTopChannel:
        filehandle.write('%s\n' % listitem)
time.sleep(15)

API_ENDPOINT = 'https://api.twitch.tv/kraken/clips/top?channel=Sykkuno&period=all&trending=false&limit=100'
ID = ''
auth = 'application/vnd.twitchtv.v5+json'

head = {
'Client-ID' : ID,
'Accept' : auth
}

r = requests.get(url = API_ENDPOINT, headers = head)

twitchClipLinksTopChannel = []
data = r.json()

for link in data['clips']:
    store = str(link['url'])
    twitchClipLinksTopChannel.append(store)

for link in data['clips']:
    store = str(link['broadcaster']['display_name'])
    displayNameTopChannel.append(store)

for link in data['clips']:
    store = str(link['broadcaster']['channel_url'])
    displayNameLinkTopChannel.append(store)

for link in data['clips']:
    store = str(link['views'])
    viewsTopChannel.append(store)

for link in data['clips']:
    store = str(link['curator']['display_name'])
    clipCreatorNameTopChannel.append(store)

for link in data['clips']:
    store = str(link['curator']['channel_url'])
    clipCreatorLinkTopChannel.append(store)

for link in data['clips']:
    store = str(link['created_at'])
    clipUploadTimeTopChannel.append(store)


with open('apiTwitchClipLinksTopChannel.py', 'w') as filehandle:
    for listitem in twitchClipLinksTopChannel:
        filehandle.write('%s\n' % listitem)

with open('apiDisplayNameTopChannel.py', 'w') as filehandle:
    for listitem in displayNameTopChannel:
        filehandle.write('%s\n' % listitem)

with open('apiDisplayNameLinkTopChannel.py', 'w') as filehandle:
    for listitem in displayNameLinkTopChannel:
        filehandle.write('%s\n' % listitem)

with open('apiViewsTopChannel.py', 'w') as filehandle:
    for listitem in viewsTopChannel:
        filehandle.write('%s\n' % listitem)

with open('apiClipCreatorNameTopChannel.py', 'w') as filehandle:
    for listitem in clipCreatorNameTopChannel:
        filehandle.write('%s\n' % listitem)

with open('apiClipCreatorLinkTopChannel.py', 'w') as filehandle:
    for listitem in clipCreatorLinkTopChannel:
        filehandle.write('%s\n' % listitem)

with open('apiClipUploadTimeTopChannel.py', 'w') as filehandle:
    for listitem in clipUploadTimeTopChannel:
        filehandle.write('%s\n' % listitem)

print('Urls stored in List')
