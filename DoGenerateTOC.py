from constants import *
from other import *

class DoGenerateTOC:
    def __init__(self, fileCacheTOC, fileCacheVisit):
        self.fileCacheTOC = fileCacheTOC
        self.fileCacheVisit = fileCacheVisit
        self.out = []

    def execute(self):
        lines = readFileLines(self.fileCacheVisit)
        dates = parseArticleDates(lines)
        points = generateNavPoints(dates)
        toc = TEMPLATE_TOC.replace("%TOC%", points)
        self.print(toc)
        writeFileLines(self.fileCacheTOC, self.out)

    def print(self, s):
        self.out.append(s)
        #print(s)
