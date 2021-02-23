from janome.tokenizer import Tokenizer


class TweetModel:
    """Tweet model"""

    generic_words = ['RT', 'https', 'jp', 'co', 'amp']

    def __init__(self, id, text, author_id):
        self.id = id
        self.text = text
        self.author_id = author_id

    @property
    def tokenize(self):
        tokenizer = Tokenizer()
        return tokenizer.tokenize(self.text)

    @property
    def word_list(self):
        return [token.surface for token in self.tokenize]

    @property
    def noun_list(self):
        filtered = filter(self.filter_word, self.tokenize)
        return [token.surface for token in filtered]

    def filter_word(self, x):
        is_noun = x.part_of_speech.startswith('名詞,固有名詞') or x.part_of_speech.startswith('名詞,一般')
        is_original = x.surface not in self.generic_words and len(x.surface) != 1
        return is_noun and is_original
