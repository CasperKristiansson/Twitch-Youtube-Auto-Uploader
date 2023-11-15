# Automatically Upload Twitch Clips to YouTube
This repository enables you to automatically upload Twitch clips from various categories directly to YouTube. To ensure a smooth setup and execution, it's highly recommended to read through all the instructions carefully before implementing this program on your device.

## Step 1: Create a Twitch Developer Account and Fetch Videos, Data
1. Sign up for a Twitch Developer account at Twitch Developer Portal https://dev.twitch.tv/.
2. In the console tab, create a new application. Set a custom name for your application and use "http://localhost" as the redirect URL (OAuth). Choose 'Website Integration' as the category.
3. Upon creating your application, a credential file will be generated. Copy the Client ID from this file and paste it into the twitch_credentials.py file in our repository.
4. Decide on the categories of Twitch clips you want to fetch. Remember, YouTube has a limit of uploading 6 videos per day, so set the maximum number of videos to 6. Refer to the Twitch API documentation for more details https://dev.twitch.tv/docs/api/reference/.

Here is an example:

```bash
https://api.twitch.tv/kraken/clips/top?game=League%20of%20Legends&period=day&trending=false&limit=6&language=en
```

## Step 2: Set Up Google Credentials
1. Visit Google Cloud Console (https://console.cloud.google.com/) and log in with your Google account.
2. Create a new project via the upper left corner menu.
3. Navigate to 'APIs & Services' > 'Credentials', then create a new credential as an “OAuth client ID” with the application type set to “Desktop app”.
4. Download the credential data as a JSON file, which will be used in the setup process.


## Step 3: Completing Google's Audit Process
Google requires an audit for remote video uploads for security reasons. This process can be time-consuming:

1. Thoroughly review Google's terms of service and API revision history.
2. Submit your application for an audit at YouTube API Audit Form https://support.google.com/youtube/contact/yt_api_form.
3. Be prepared for potential follow-up requests via email. It might take multiple communications before your application is approved.

![Twitch Developer Console](images/image2.png)

## Step 4: Installation Requirements
Ensure you have the following:

1. The latest version of Python installed on your device.
2. Run the command pip install -r requirements.txt in your terminal to install the necessary dependencies.


## Additional Resources

### Troubleshooting Links
- YouTube API Upload Guide https://developers.google.com/youtube/v3/guides/uploading_a_video
- Twitch Basic Troubleshooting https://help.twitch.tv/s/article/basic-troubleshooting-tips?language=en_US
- YouTube API Videos Insert Documentation https://developers.google.com/youtube/v3/docs/videos/insert

### Disclaimer
When using this tool to upload videos to YouTube, ensure that you comply with both Twitch's and YouTube's guidelines. Use this tool at your own risk.
