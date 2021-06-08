import pymongo
from .env import ENV
from bson.json_util import dumps, loads


class DB():

    YOUTUBE_CLXN = 'yt_data'

    mongoc = pymongo.MongoClient(ENV['MONGO_URI'])

    def __init__(self):
        self.db = self.mongoc[ENV['DB']]

    def find(self, clxn, filter = {}, projection = {'_id':0}, docs_cnt = 0, skip=0):
        return loads(dumps(self.db[clxn].find(filter, projection,
                                              sort=[('_id', pymongo.DESCENDING)]).skip(skip).limit(docs_cnt)))

    def find_one(self, clxn, filter = {}):
        return self.db[clxn].find_one(filter)

    def update_one(self, clxn, filter, update):
        return self.db[clxn].update_one(filter, update)

    def insert(self, clxn, data):
        return self.db[clxn].insert(data)

    def remove(self, clxn, filter = {}):
        return self.db[clxn].remove(filter)

    def find_latest(self, clxn, filter = {}):
        return self.db[clxn].find_one(filter, sort=[('_id', pymongo.DESCENDING)])


