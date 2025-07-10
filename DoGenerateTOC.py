from constants import *
from other import *

class DoGenerateTOC:
    def __init__(self, fileCacheContent, fileCacheTOC):
        self.fileCacheContent = fileCacheContent
        self.fileCacheTOC = fileCacheTOC
        self.out = []

    def execute(self):
        lines = readFileLines(self.fileCacheContent)
        datesTitles = parseArticleDatesAndTitles(lines)
        points = generateNavPoints(datesTitles)
        toc = TEMPLATE_TOC.replace("%TOC%", points)
        self.print(toc)
        writeFileLines(self.fileCacheTOC, self.out)

    def print(self, s):
        self.out.append(s)
        #print(s)
