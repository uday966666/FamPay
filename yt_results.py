import os
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2 import service_account


scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def main():

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    scopes = ['https://www.googleapis.com/auth/youtube']
    service_account_file = 'service.json'

    credentials = service_account.Credentials.from_service_account_file(
        service_account_file, scopes=scopes)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        part="snippet",
        order="date",
        pageToken="CAUQAA",
        publishedAfter="2021-06-07T00:00:00Z",
        q="jabardasth",
        type="video"
    )
    response = request.execute()

    print(response)


if __name__ == "__main__":
    main()
