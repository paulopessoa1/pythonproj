import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "secrets.json" #mude seu .json para secrets.json

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file( 
        client_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=25,
        playlistId="PLBCF2DAC6FFB574DE"
    )
    response = request.execute()
    videos = response['items']
    ids_video = [video['contentDetails']['videoId']  for video in videos]
    request = youtube.videos().list(
       part ="snippet,statistics",
       id = ",".join(ids_video)
   )
    response = request.execute()
    videos = response['items']
    for video in videos:
        ids_video = video['id']
        views = video['statistics']['viewCount']
        title = video['snippet']['title']
        print(f'titulo: {title} - views: {views} - id: {ids_video}')
if __name__ == "__main__":
    main()