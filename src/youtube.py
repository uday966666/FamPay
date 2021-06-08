from .db import DB


class Youtube:

    def __init__(self):
        pass

    def insert(self, data):
        DB().insert(DB.YOUTUBE_CLXN, data)

    def get_results(self, filters):
        start = int(filters.get('start', 0))
        per_page = int(filters.get('perPage', 20))
        # Page = int(filters.get('page', 1))
        data = list(DB().find(DB.YOUTUBE_CLXN, {}, skip=start, docs_cnt=per_page))
        result = {'details': data, 'pagination': self.get_pagination(start, per_page, data)}
        return result

    def get_latest_record(self, filters):
        return DB().find_latest(DB.YOUTUBE_CLXN, filters)

    def get_pagination(self, skip, docs_cnt, data):
        result = {'pageSize': docs_cnt, 'start': len(data) + skip, 'totalRecorsInPage': len(data)}
        return result

    def get_search_results(self, search_q: str):
        element_string = search_q.strip().split(" ")
        regx = "*".join(element_string)
        regex = regx + "*"
        filter = {
            "$or": [
                {
                    "title":
                        {
                            "$regex": regex, "$options": 'i'
                        }
                },

                {
                    "description":
                        {
                            "$regex": regex, "$options": 'i'}}
            ]
        }
        data = list(DB().find(DB.YOUTUBE_CLXN, filter))
        return data






