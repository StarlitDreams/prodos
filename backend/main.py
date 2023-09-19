from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns

#set up mathplot lib
import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')

# Read yt_key and save it into a variable
with open('yt_key.txt', 'r') as f:
    api_key = f.read()
channel_id = 'UCX6OQ3DkcsbYNE6H8uQQuVA'

# Build the service
youtube = build('youtube', 'v3', developerKey=api_key)

# Function to get channel statistics
def get_channel_statistics(youtube, channel_id):
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
        playlist_id=response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    )
    return data
     
channel_statistics = get_channel_statistics(youtube, channel_id)

# Create a DataFrame from the dictionary
channel_data = pd.DataFrame([channel_statistics])

# Drop the 'description' and 'country' columns
channel_data = channel_data.drop(columns=['description', 'country'])

# Setting the correct data types for each column
channel_data['Subscribers'] = pd.to_numeric(channel_data['Subscribers'])
channel_data['Views'] = pd.to_numeric(channel_data['Views'])
channel_data['Total_Videos'] = pd.to_numeric(channel_data['Total_Videos'])

print(channel_data)

"""
# Print the resulting DataFrame
sns.set(rc={'figure.figsize':(11.7,8.27)})
ax = sns.barplot(x='Channel_name', y='Subscribers', data=channel_data)
plt.show()  # Display the plot
"""

#get the video ids
def get_channel_videos(youtube, playlist_id):
    videos = []
    next_page_token =  None
    
    while 1:
        request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=playlist_id, 
            maxResults=50, 
            pageToken=next_page_token
        )
        
        response = request.execute()
        
        # Iterate through the items and extract video IDs
        for item in response['items']:
            video_id = item['contentDetails']['videoId']
            videos.append(video_id)
        
        next_page_token = response.get('nextPageToken')
        
        if next_page_token is None:
            break
    
    return videos


video_ids = get_channel_videos(youtube, channel_data['playlist_id'][0])


 
def get_video_details(youtube, video_ids):
    all_video_stats = []
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part='snippet,contentDetails,statistics',
            id=','.join(video_ids[i:i+50]))
        response = request.execute() 
        for video in response['items']:
            video_stats = dict(
                Title=video['snippet']['title'],
                publishedAt=video['snippet']['publishedAt'],
                viewCount=video['statistics'].get('viewCount', 0),
                likeCount=video['statistics'].get('likeCount', 0),
                dislikeCount=video['statistics'].get('dislikeCount', 0),
                commentCount=video['statistics'].get('commentCount', 0)
            )
            
            all_video_stats.append(video_stats)
    return all_video_stats


video_details = get_video_details(youtube,video_ids)
video_data = pd.DataFrame(video_details)
video_data['publishedAt'] = pd.to_datetime(video_data['publishedAt'])
video_data['viewCount'] = pd.to_numeric(video_data['viewCount'])
video_data['likeCount'] = pd.to_numeric(video_data['likeCount'])
video_data['dislikeCount'] = pd.to_numeric(video_data['dislikeCount'])

print("His videos: ")
print(video_data)

print("Their most viewed video: ")
top_10 = video_data.sort_values(by='viewCount', ascending=False).head(10)
print(top_10)
#ax1=sns.barplot(y='Title', x='viewCount', data=top_10)

video_data['Month']=pd.to_datetime(video_data['publishedAt']).dt.strftime('%b') 
videos_per_month = video_data.groupby('Month', as_index=False).size()
sort_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create the bar plot
ax2 = sns.barplot(x='Month', y='size', data=videos_per_month, order=sort_order)
plt.show()