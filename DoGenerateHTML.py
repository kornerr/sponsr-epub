from constants import *
from other import *

class DoGenerateHTML:
    def __init__(self, fileCacheCollect, fileCacheHTML):
        self.fileCacheCollect = fileCacheCollect
        self.fileCacheHTML = fileCacheHTML
        self.out = []

    def execute(self):
        lines = readFileLines(self.fileCacheCollect)
        articles = parseCollectedArticles(lines)
        html = generateHTML(articles)
        self.print(html)
        writeFileLines(self.fileCacheHTML, self.out)

    def print(self, s):
        self.out.append(s)
        #print(s)
