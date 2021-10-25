import requests
import pandas
import twitch_credentials
import video_information

def get_data():
    api_endpoint = f'https://api.twitch.tv/kraken/clips/top?game={video_information.game_name}&period=day&trending=false&limit=6&language=en'
    head = {'Client-ID' : twitch_credentials.ID, 'Accept' : 'application/vnd.twitchtv.v5+json'}

    data = requests.get(url = api_endpoint, headers = head)

    return data.json()

def save_data(data):
    df = pandas.DataFrame(data['clips'])
    df.to_excel('twitch_data.xlsx')

def main():
    data = get_data()
    save_data(data)

if __name__ == '__main__':
    main()
