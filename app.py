from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler

import atexit

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
   return "Server is Up and Running :D"


@app.route('/getResults', methods=['GET'])
def get_results():

    pass


@app.route('/searchResults', methods=['GET'])
def get_search_results():
    search_text = request.args.get('search')
    return search_text


def get_yt_results():
    # query YT with keyword

    pass


scheduler = BackgroundScheduler()
scheduler.add_job(func=get_yt_results, trigger="interval", seconds=10)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
   app.run()