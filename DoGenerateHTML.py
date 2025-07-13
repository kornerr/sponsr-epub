from constants import *
from other import *

class DoGenerateHTML:
    def __init__(self, fileCacheContent, fileCacheHTML):
        self.fileCacheContent = fileCacheContent
        self.fileCacheHTML = fileCacheHTML
        self.out = []

    def execute(self):
        lines = readFileLines(self.fileCacheContent)
        contents = parseArticleContents(lines)
        datesTitles = parseArticleDatesAndTitles(lines)
        html = generateHTML(datesTitles, contents)
        self.print(html)
        writeFileLines(self.fileCacheHTML, self.out)

    def print(self, s):
        self.out.append(s)
        #print(s)
