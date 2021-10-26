import pandas
import os
import video_information
import ast

class Video:
    def __init__(self):
        self.df = pandas.read_excel('twitch_data.xlsx', sheet_name='Sheet1')
        
        self.upload_time = self.df['created_at'][0].replace('T', ' ').replace('Z', '')
        self.streamer_name = ast.literal_eval(self.df['broadcaster'][0])['display_name']
        self.streamer_link = ast.literal_eval(self.df['broadcaster'][0])['channel_url']
        self.views = self.df['views'][0]
        self.clip_creator_name = ast.literal_eval(self.df['curator'][0])['display_name']
        self.clip_creator_link = ast.literal_eval(self.df['curator'][0])['channel_url']

        self.description = f"""
►Credit
name: {self.streamer_name}
Twitch Link: {self.streamer_link}

►Clip Creator
name: {self.clip_creator_name}
Twitch Link: {self.clip_creator_link}

►Clip Stats
Views At Upload: {self.views}
Date and Time: {self.upload_time}
"""

        self.category = "24"
        self.keywords = video_information.keywords
        self.privacyStatus = "public"

    def getFileName(self, type):
        for file in os.listdir("Video"):
            if type == "video":
                return file
