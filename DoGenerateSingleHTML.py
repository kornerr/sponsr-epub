from constants import *
from other import *

class DoGenerateSingleHTML:
    def __init__(self, fileCacheCollect, targetDate):
        self.fileCacheCollect = fileCacheCollect
        self.out = []
        self.targetDate = targetDate

    def execute(self):
        lines = readFileLines(self.fileCacheCollect)
        articles = parseCollectedArticles(lines)
        for a in articles:
            dt = a.date.split("T")[0]
            if dt == self.targetDate:
                html = generateHTML([a])
                fileName = TEMPLATE_SINGLE_HTML_FILE.replace("%DATE%", dt)
                writeFileLines(fileName, [html])

    def print(self, s):
        self.out.append(s)
        print(s)
