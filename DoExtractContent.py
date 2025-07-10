from constants import *
from other import *

class DoExtractContent:
    def __init__(self, fileCacheContent, fileCacheVisit):
        self.fileCacheContent = fileCacheContent
        self.fileCacheVisit = fileCacheVisit
        self.out = []

    def execute(self):
        lines = readFileLines(self.fileCacheVisit)
        articles = parseArticles(lines)
        for key in articles:
            (dt, title) = key.split("/")
            content = articles[key]
            self.print(ARTICLE_PREFIX_DATE + dt)
            self.print(ARTICLE_PREFIX_TITLE + title)
            self.print(ARTICLE_PREFIX_CONTENT + content)
        writeFileLines(self.fileCacheContent, self.out)

    def print(self, s):
        self.out.append(s)
        #print(s)
