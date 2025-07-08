from constants import *
from other import *

class DoGenerateContent:
    def __init__(self, fileCacheVisit):
        self.fileCacheVisit = fileCacheVisit
        self.out = []

    def execute(self):
        lines = readFileLines(self.fileCacheVisit)
        self.print("TODO")

    def print(self, s):
        self.out.append(s)
        print(s)
