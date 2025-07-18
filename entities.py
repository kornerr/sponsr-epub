from constants import *

class Article:
    def __init__(self):
        self.date = None
        self.id = None
        self.nextId = None
        self.text = None
        self.title = None
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return f"{ARTICLE_PREFIX_DATE}{self.date}\n{ARTICLE_PREFIX_TITLE}{self.title}\n{ARTICLE_PREFIX_ID}{self.id}\n{ARTICLE_PREFIX_NEXT_ID}{self.nextId}\n{ARTICLE_PREFIX_TEXT}{self.text}"
