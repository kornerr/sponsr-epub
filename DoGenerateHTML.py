from constants import *
from other import *

class DoGenerateHTML:
    def __init__(self, fileCacheCollect):
        self.fileCacheCollect = fileCacheCollect
        self.out = []

    def execute(self):
        lines = readFileLines(self.fileCacheCollect)
        articles = parseCollectedArticles(lines)
        segmentedArticles = articlesByYear(articles)
        for year in segmentedArticles: 
            articles = segmentedArticles[year]
            html = generateHTML(articles)
            fileName = TEMPLATE_HTML_FILE.replace("%YEAR%", year)
            writeFileLines(fileName, [html])

    def print(self, s):
        self.out.append(s)
        print(s)
