from googleapiclient.discovery import build
import openai
import os
import requests
from datetime import datetime, timedelta
import google.oauth2.credentials
from google.oauth2 import service_account


def read_api_key(filename):
    with open(filename, 'r') as file:
        gpt_api_key = file.readline().strip()  
    return gpt_api_key
openai.api_key  = read_api_key("gpt_api_key.txt")


#Gives the service description
messages = [
    {
        "role": "system",
        "content": "You are a personal assistat which analyzes youtube analytics. You shall analyze the youtube analytics of a channel. \
            I shall provide you with the channel name, description, subscriberCount, views, videoCount and region. \
            Keep a professional tone while describing the channel. "
    }
    ]


with open('yt_key.txt', 'r') as f:
    api_key = f.read()
youtube_api_key = read_api_key("yt_key.txt")
channel_id = 'UCX6OQ3DkcsbYNE6H8uQQuVA'

# Build the service
youtube = build('youtube', 'v3', developerKey=api_key)

# Function to get channel statistics
request = youtube.channels().list(
part='snippet,contentDetails,statistics', 
id=channel_id)
response = request.execute()
    
data = dict(
        Channel_name=response['items'][0]['snippet']['title'],
        Subscribers=response['items'][0]['statistics']['subscriberCount'],
        Views=response['items'][0]['statistics']['viewCount'],
        Total_Videos=response['items'][0]['statistics']['videoCount'],
        description=response['items'][0]['snippet']['description'],
        country=response['items'][0]['snippet']['country'],
    )

messages.append({"role": "user", "content": "The channel name is " + data['Channel_name'] + "."})
messages.append({"role": "user", "content": "The channel description is " + data['description'] + "."})
messages.append({"role": "user", "content": "The channel has " + data['Subscribers'] + " subscribers."})
messages.append({"role": "user", "content": "The channel has " + data['Views'] + " views."})
messages.append({"role": "user", "content": "The channel has " + data['Total_Videos'] + " videos."})
messages.append({"role": "user", "content": "The channel is from " + data['country'] + "."})



"""

chat = openai.ChatCompletion.create( 
                                    model="gpt-3.5-turbo", messages=messages,temperature=0.7, max_tokens=450
        )
reply = chat.choices[0].message.content
print(reply)
"""