from __future__ import unicode_literals
import requests
import os
import shutil
import glob
import twitch_credentials

def delete():
    files = os.listdir(os.curdir)
    for file in files:
        if '.txt' in file:
            shutil.move(file, 'txtFiles')

    files = glob.glob('txtFiles\\*')
    for f in files:
        os.remove(f)

def get_data():
    API_ENDPOINT = 'https://api.twitch.tv/kraken/clips/top?game=League%20of%20Legends&period=day&trending=false&limit=6&language=en'
    auth = 'application/vnd.twitchtv.v5+json'

    head = {
    'Client-ID' : twitch_credentials.ID,
    'Accept' : auth
    }

    r = requests.get(url = API_ENDPOINT, headers = head)
    data = r.json()

    return data

def save_data(data):
    displayName = []
    displayNameLink = []
    views = []
    clipCreatorName = []
    clipCreatorLink = []
    clipUploadTime = []
    currentFile = []
    twitchClipLinks = []
    current_file = []

    for link in data['clips']:
        store = str(link['url'])
        twitchClipLinks.append(store)

    for link in data['clips']:
        store = str(link['broadcaster']['display_name'])
        displayName.append(store)

    for link in data['clips']:
        store = str(link['broadcaster']['channel_url'])
        displayNameLink.append(store)

    for link in data['clips']:
        store = str(link['views'])
        views.append(store)

    for link in data['clips']:
        store = str(link['curator']['display_name'])
        clipCreatorName.append(store)

    for link in data['clips']:
        store = str(link['curator']['channel_url'])
        clipCreatorLink.append(store)

    for link in data['clips']:
        store = str(link['created_at'])
        clipUploadTime.append(store)

    with open('apiTwitchClipLinks.txt', 'w') as filehandle:
        for listitem in twitchClipLinks:
            filehandle.write('%s\n' % listitem)

    with open('apiDisplayName.txt', 'w') as filehandle:
        for listitem in displayName:
            filehandle.write('%s\n' % listitem)

    with open('apiDisplayNameLink.txt', 'w') as filehandle:
        for listitem in displayNameLink:
            filehandle.write('%s\n' % listitem)

    with open('apiViews.txt', 'w') as filehandle:
        for listitem in views:
            filehandle.write('%s\n' % listitem)

    with open('apiClipCreatorName.txt', 'w') as filehandle:
        for listitem in clipCreatorName:
            filehandle.write('%s\n' % listitem)

    with open('apiClipCreatorLink.txt', 'w') as filehandle:
        for listitem in clipCreatorLink:
            filehandle.write('%s\n' % listitem)

    with open('apiClipUploadTime.txt', 'w') as filehandle:
        for listitem in clipUploadTime:
            filehandle.write('%s\n' % listitem)

    with open('currentFile.txt', 'w') as filehandle:
        for listitem in currentFile:
            filehandle.write('%s\n' % listitem)

if __name__ == '__main__':
    delete()
    DATA = get_data()
    #save_data(DATA)
