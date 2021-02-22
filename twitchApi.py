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

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


API_ENDPOINT = 'https://api.twitch.tv/kraken/clips/top?channel=Cyberpunk%202077&period=all&trending=false&limit=100'
ID = ''
auth = 'application/vnd.twitchtv.v5+json'

head = {
'Client-ID' : ID,
'Accept' : auth
}

r = requests.get(url = API_ENDPOINT, headers = head)

twitchClipLinksLOL = []
data = r.json()