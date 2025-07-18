import time
from constants import *
from entities import *
from other import *

class DoCollectArticles:
    def __init__(self, fileCache):
        self.fileCache = fileCache
        self.drv = None
        self.out = []

    def execute(self):
        url = BASE_URL + FIRST_POST
        html = webPageHTML(url)

        a = Article()
        a.date = parseArticleDate(html)
        a.id = parseArticleId(html)
        a.nextId = parseArticleNextId(html)
        a.text = parseArticleText(html)
        a.title = parseArticleTitle(html)

        self.print(a)

    def print(self, s):
        self.out.append(s)
        print(s)

