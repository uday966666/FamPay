import os
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2 import service_account
from .youtube import Youtube

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

SEARCH_STRING = 'football'


def get_yt_data(published_after, search_string=SEARCH_STRING):

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
        publishedAfter=published_after,
        q=search_string,
        type="video"
    )
    response = request.execute()
    return response
    # print(response)


def get_published_after():
    youtube = Youtube()
    latest_record = youtube.get_latest_record(filters={})

    return latest_record.get('publishedAt')


def poll_yt_data():
    """

    :return:
    """
    required_data = get_yt_data(published_after=get_published_after()).get('items')

    for doc in required_data:
        processec_data = get_processed_doc(doc)
        youtube = Youtube()
        youtube.insert(data=processec_data)
        print(processec_data)


def get_processed_doc(doc):

    processed_value= {}
    snippet = doc.get('snippet')
    processed_value['title'] = snippet.get('title')
    processed_value['publishedAt'] = snippet.get('publishedAt')
    processed_value['description'] = snippet.get('description')
    processed_value['thumbnails'] = snippet.get('thumbnails')
    processed_value['key_word'] = 'jabardasth'

    return processed_value


# if __name__ == "__main__":

