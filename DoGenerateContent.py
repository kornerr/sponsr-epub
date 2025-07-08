from constants import *
from other import *

class DoGenerateContent:
    def __init__(self, fileCacheVisit):
        self.fileCacheVisit = fileCacheVisit
        self.out = []

    def execute(self):
        lines = readFileLines(self.fileCacheVisit)
        articles = parseArticles(lines)
        self.print(articles)

    def print(self, s):
        self.out.append(s)
        print(s)
