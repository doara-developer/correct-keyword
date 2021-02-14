import requests
from urllib import parse
from datetime import datetime, timedelta, timezone

from models.tweet import TweetModel
from models.search_result import SearchResultModel


class Search:

    API_URL = 'https://api.twitter.com/2/tweets/search/recent'

    def __init__(self, api_key):
        self.api_key = api_key

        # Set API Key
        self.session = requests.Session()
        self.session.headers['Authorization'] = 'Bearer ' + self.api_key

    def search(self, keyword):
        """Search recent tweets"""
        query = {
            'max_results': 100,
            'query': keyword,
            'tweet.fields': 'author_id,text',
            'start_time': self._create_start_time(15)
        }
        url_query = parse.urlencode(query)
        res = self.session.get(self.API_URL + '?' + url_query)
        res_json = res.json()
        tweet_list = [TweetModel(id=item['id'], text=item['text'], author_id=item['author_id']) for item in res_json['data']]
        return SearchResultModel(tweet_list=tweet_list)

    def _create_start_time(self, minutes):
        """create start time"""
        dt_now = datetime.now(timezone.utc)
        start_time = str(dt_now - timedelta(minutes=minutes))
        return start_time.replace('+00:00', 'Z').replace(' ', 'T')
