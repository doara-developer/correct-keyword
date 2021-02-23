class SearchWordListModel:
    """SearchWordModel model"""

    def __init__(self):
        self.word_list = []

    def __iter__(self):
        for word in self.word_list:
            yield word

    def __str__(self):
        ret = []
        for word in self.word_list:
            ret.append(str(word))
        return str(ret)

    def add(self, word):
        res = self.find(word)
        if res is None:
            self.word_list.append(SearchWordModel(word))
        else:
            res.count_up()

    def find(self, word):
        for model in self.word_list:
            if model.id == word:
                return model
        return None

    def sort(self):
        self.word_list = sorted(self.word_list, key=lambda x: x.count, reverse=True)


class SearchWordModel:
    """SearchWordModel model"""

    def __init__(self, id):
        self.id = id
        self.count = 1

    def __str__(self):
        ret = {
            'id': self.id,
            'count': self.count,
        }
        return str(ret)

    def count_up(self):
        self.count += 1
