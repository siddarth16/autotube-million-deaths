import os
import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def authenticate_youtube():
    creds = None

    # token.pickle stores the user's access and refresh tokens
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            "client_secrets.json", SCOPES)
        creds = flow.run_console()
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)
    return youtube

def upload_video(video_path, title, description):
    youtube = authenticate_youtube()

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": f"{title} #Shorts",
                "description": description,
                "tags": ["weird deaths", "bizarre", "1 million ways to die", "strange history"],
                "categoryId": "24"  # Entertainment
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=googleapiclient.http.MediaFileUpload(video_path)
    )

    response = request.execute()
    print("✅ Uploaded:", response["id"])

# Example run
if __name__ == "__main__":
    upload_video(
        video_path="tmp/final_video.mp4",
        title="One of the Strangest Ways to Die",
        description="This bizarre death will leave you stunned... \n\n#1MillionWaysToDie"
    )
