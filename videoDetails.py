import os
from googleapiclient.http import MediaFileUpload

twitchClipLinks = []
displayName = []
displayNameLink = []
views = []
clipCreatorName = []
clipCreatorLink = []
clipUploadTime = []
currentFile = []
currentFileLength = []

with open('currentFile.txt', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        currentFile.append(currentPlace)

with open('apiTwitchClipLinks.txt', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        twitchClipLinks.append(currentPlace)

with open('apiDisplayName.txt', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        displayName.append(currentPlace)

with open('apiDisplayNameLink.txt', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        displayNameLink.append(currentPlace)

with open('apiViews.txt', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        views.append(currentPlace)

with open('apiClipCreatorName.txt', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        clipCreatorName.append(currentPlace)

with open('apiClipCreatorLink.txt', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        clipCreatorLink.append(currentPlace)

with open('apiClipUploadTime.txt', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        clipUploadTime.append(currentPlace)

currentFileLength = len(currentFile)


class Video:
    def __init__(self):
        clipUpTime = clipUploadTime[currentFileLength]
        newtime = clipUpTime.replace('T', ' ')

        streamerName = displayName[currentFileLength]
        streamerLink = displayNameLink[currentFileLength]
        clipViews = views[currentFileLength]
        clipCreatorNam = clipCreatorName[currentFileLength]
        clipCreatorlin = clipCreatorLink[currentFileLength]
        resultClipTime = newtime.replace('Z', '')

        self.description = f"""
►Credit
name: {streamerName}
Twitch Link: {streamerLink}

►Clip Creator
name: {clipCreatorNam}
Twitch Link: {clipCreatorlin}

►Clip Stats
Views At Upload: {clipViews}
Date and Time: {resultClipTime}
"""

        self.category = "24"
        self.keywords = "sykkuno,corpse and sykkuno,sykkuno among us,sykkuno and corpse,corpse and sykkuno among us,sykkuno imposter win,sykkuno proximity chat among us,sykkuno sad,sykkuno imposter round,sykkuno valkyrae,sykkuno babushka,sykkuno offlinetv,sykkuno toast,sykkuno crying,sykkuno and corpse imposter,sykkuno age,lily sykkuno,sykkuno cries,sykkuno troll,among us sykkuno,sykkuno and valkyrae imposter,valkyrae sykkuno,how old is sykkuno,sykkuno valorant"
        self.privacyStatus = "public"

    def getFileName(self, type):
        for file in os.listdir("Video"):
            if type == "video" and file.split(".", 1)[1] != "jpg":
                return file
                break
            elif type == "thumbnail" and file.split(".", 1)[1] != "mp4":
                return file
                break

    def insertThumbnail(self, youtube, videoId):
        thumnailPath = "Video\\{}".format(self.getFileName("thumbnail"))

        request = youtube.thumbnails().set(
            videoId=videoId,
            media_body=MediaFileUpload(thumnailPath)
        )
        response = request.execute()
        print(response)
