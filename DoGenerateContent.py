from constants import *
from other import *

class DoGenerateContent:
    def __init__(self, fileCacheContent, fileCacheHTMLContent):
        self.fileCacheContent = fileCacheContent
        self.fileCacheHTMLContent = fileCacheHTMLContent
        self.out = []

    def execute(self):
        lines = readFileLines(self.fileCacheContent)
        contents = parseArticleContents(lines)
        datesTitles = parseArticleDatesAndTitles(lines)
        html = generateHTMLContent(datesTitles, contents)
        self.print(html)
        writeFileLines(self.fileCacheHTMLContent, self.out)

    def print(self, s):
        self.out.append(s)
        #print(s)
