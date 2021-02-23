from models.search_word import SearchWordListModel


class SearchResultModel:
    """SearchResultModel model"""

    def __init__(self):
        self.tweet_list = []
        self.result = None

    @property
    def total(self):
        return len(self.tweet_list)

    @property
    def word_list(self):
        if self.result is not None:
            return self.result

        self.result = SearchWordListModel()
        for tweet in self.tweet_list:
            self._update_list(self.result, tweet.noun_list)

        self.result.sort()
        return self.result

    def append_list(self, tweet_list):
        self.tweet_list.extend(tweet_list)

    def _update_list(self, result, word_list):
        for word in word_list:
            result.add(word)
