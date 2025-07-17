from constants import *

class Article:
    def __init__(self):
        self.date = None
        self.next = None
        self.src = None
        self.title = None
        self.url = None
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return f"{ARTICLE_PREFIX_DATE}{self.date}\n{ARTICLE_PREFIX_TITLE}{self.title}\n{ARTICLE_PREFIX_URL}{self.url}\n{ARTICLE_PREFIX_NEXT}{self.next}\n{ARTICLE_PREFIX_SRC}{self.src}"
