import os
from googleapiclient.http import MediaFileUpload

twitchClipLinksTopChannel = []
displayNameTopChannel = []
displayNameLinkTopChannel = []
viewsTopChannel = []
clipCreatorNameTopChannel = []
clipCreatorLinkTopChannel = []
clipUploadTimeTopChannel = []
currentFileTopChannel = []
currentFileLengthTopChannel = []


with open('currentFileTopChannel.py', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        currentFileTopChannel.append(currentPlace)

with open('apiTwitchClipLinksTopChannel.py', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        twitchClipLinksTopChannel.append(currentPlace)

with open('apiDisplayNameTopChannel.py', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        displayNameTopChannel.append(currentPlace)

with open('apiDisplayNameLinkTopChannel.py', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        displayNameLinkTopChannel.append(currentPlace)

with open('apiViewsTopChannel.py', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        viewsTopChannel.append(currentPlace)

with open('apiClipCreatorNameTopChannel.py', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        clipCreatorNameTopChannel.append(currentPlace)

with open('apiClipCreatorLinkTopChannel.py', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        clipCreatorLinkTopChannel.append(currentPlace)

with open('apiClipUploadTimeTopChannel.py', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        clipUploadTimeTopChannel.append(currentPlace)

currentFileLength = len(currentFileTopChannel)


class Video:
    def __init__(self):
        clipUpTime = clipUploadTimeTopChannel[currentFileLength]
        newtime = clipUpTime.replace('T', ' ')

        streamerName = displayNameTopChannel[currentFileLength]
        streamerLink = displayNameLinkTopChannel[currentFileLength]
        clipViews = viewsTopChannel[currentFileLength]
        clipCreatorNam = clipCreatorNameTopChannel[currentFileLength]
        clipCreatorlin = clipCreatorLinkTopChannel[currentFileLength]
        resultClipTime = newtime.replace('Z', '')

        self.description = f"""
Disclaimer: I own none of these clips and all of them are from the respective owner. If you want anything removed contact johnnybravaski@gmail.com

►Credit
name: {streamerName}
Twitch Link: {streamerLink}

►Clip Creator
name: {clipCreatorNam}
Twitch Link: {clipCreatorlin}

►Clip Stats
Views At Upload: {clipViews}
Date and Time: {resultClipTime}

Just started out this channel and I hope you can show me some support! I plan to continue to post a lot of content these upcoming months and reach 1000 Subscribers at the end of the year. I hope I can reach this goal and that you can become a part of it. This whole process of collecting videos, editing, and optimizing videos is a big passion of mine.

► Don't forget to subscribe for more content!
► If you want to see more make sure to comment, like, and turn on all notifications! 

Disclaimer: I own none of these clips and all of them are from the respective owner. If you want anything removed contact johnnybravaski@gmail.com
"""

        self.category = "24"
        self.keywords = "sykkuno,corpse and sykkuno,sykkuno among us,sykkuno and corpse,corpse and sykkuno among us,sykkuno imposter win,sykkuno proximity chat among us,sykkuno sad,sykkuno imposter round,sykkuno valkyrae,sykkuno babushka,sykkuno offlinetv,sykkuno toast,sykkuno crying,sykkuno and corpse imposter,sykkuno age,lily sykkuno,sykkuno cries,sykkuno troll,among us sykkuno,sykkuno and valkyrae imposter,valkyrae sykkuno,how old is sykkuno,sykkuno valorant"
        self.privacyStatus = "public"

    def getFileName(self, type):
        for file in os.listdir("/home/ubuntu/Youtube"):
            if type == "video" and file.split(".", 1)[1] != "jpg":
                return file
                break
            elif type == "thumbnail" and file.split(".", 1)[1] != "mp4":
                return file
                break

    def insertThumbnail(self, youtube, videoId):
        thumnailPath = "/home/ubuntu/Youtube/{}".format(self.getFileName("thumbnail"))

        request = youtube.thumbnails().set(
            videoId=videoId,
            media_body=MediaFileUpload(thumnailPath)
        )
        response = request.execute()
        print(response)
