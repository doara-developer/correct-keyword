class SearchResultModel:
    """SearchResultModel model"""

    def __init__(self, tweet_list):
        self.tweet_list = tweet_list

    @property
    def total(self):
        return len(self.tweet_list)
