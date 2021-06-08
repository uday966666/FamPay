from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from src.youtube import Youtube
from src.yt_results import get_yt_data, get_published_after, poll_yt_data


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
   return "Server is Up and Running :D"


@app.route('/getResults', methods=['GET'])
def get_results():
    yt = Youtube()
    results = yt.get_results(dict(request.args))

    return results



@app.route('/searchResults', methods=['GET'])
def get_search_results():
    search_text = request.args.get('q')
    yt = Youtube()
    search_results = yt.get_search_results(search_text)

    return str(search_results)


def get_yt_results():
    # query YT with keyword
    print("start")
    published_at = get_published_after()
    get_yt_data(published_at, 'football')
    poll_yt_data()
    print("end")


scheduler = BackgroundScheduler()
scheduler.add_job(func=get_yt_results, trigger="interval", seconds=60)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
   app.run()