
import os
from dotenv import load_dotenv

from twitter import Search

load_dotenv(verbose=True)
TWITTER_TOKEN = os.environ.get('TWITTER_TOKEN')
SEARCH_KEYWORD = os.environ.get('SEARCH_KEYWORD')

if __name__ == '__main__':
    connector = Search(TWITTER_TOKEN)
    result = connector.search(SEARCH_KEYWORD)
    print(result.total)
