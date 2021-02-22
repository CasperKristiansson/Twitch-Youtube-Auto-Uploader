import os
from googleapiclient.http import MediaFileUpload

class Video:
    def __init__(self):
        self.description = "hey"

        self.category = "24"
        self.keywords = "twitch,xqc,sliker,adept,sodapoppin,forsen,jonzherka,twitch clips,streamer,ninocentx,mizkif,maya,macaiyla,tyler1,greekgodx,cx,pokimane,clips,ludwig,poke,asmongold,shroud,tfue,summit1g,myth,trainwrecks,lsf,best of twitch,twitch highlights,funny twitch clips,twitch highlight,best of twitch today,best twitch clips,daily twitch,streaming,streamers,moments,highlights,reaction,just chatting,thicc,compilation,cute,wholesome,corpse,simp,sexy,best of,recap,sweet anita,live stream"
        self.privacyStatus = "public"

    def getFileName(self, type):
        for file in os.listdir("\\Video"):
            if type == "video" and file.split(".", 1)[1] != "jpg":
                return file
                break
            elif type == "thumbnail" and file.split(".", 1)[1] != "mp4":
                return file
                break

    def insertThumbnail(self, youtube, videoId):
        thumnailPath = "\\Video{}".format(self.getFileName("thumbnail"))

        request = youtube.thumbnails().set(
            videoId=videoId,
            media_body=MediaFileUpload(thumnailPath)
        )
        response = request.execute()
        print(response)
        