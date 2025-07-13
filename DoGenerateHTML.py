from constants import *
from other import *

class DoGenerateHTML:
    def __init__(self, fileCacheContent, fileCacheHTML):
        self.fileCacheContent = fileCacheContent
        self.fileCacheHTML = fileCacheHTML
        self.out = []

    def execute(self):
        self.print("TODO")
        lines = readFileLines(self.fileCacheContent)

    def print(self, s):
        self.out.append(s)
        print(s)
