from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns


#read yt_key and save it into a variable
with open('yt_key.txt', 'r') as f:
    api_key = f.read()
channel_id = 'UCX6OQ3DkcsbYNE6H8uQQuVA'

#build the service
youtube=build('youtube','v3',developerKey=api_key)

#Function to get channel statistics
def get_channel_statistics(youtube,channel_id):
    request=youtube.channels().list(
        part='snippet,contentDetails,statistics', 
        id=channel_id)
    response=request.execute()
    
    data= dict(Channel_name = response['items'][0]['snippet']['title'],
               Subscribers = response['items'][0]['statistics']['subscriberCount'],
               Views = response['items'][0]['statistics']['viewCount'],
               Total_Videos = response['items'][0]['statistics']['videoCount'],
               description = response['items'][0]['snippet']['description'],
               country= response['items'][0]['snippet']['country']
            )
    return response
     
get_channel_statistics(youtube,channel_id)
    
