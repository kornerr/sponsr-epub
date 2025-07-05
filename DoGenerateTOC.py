from constants import *
from other import *

class DoGenerateTOC:
    def __init__(self, fileCache):
        self.fileCache = fileCache
        self.out = []

    def execute(self):
        self.print("TODO")

    def print(self, s):
        self.out.append(s)
        print(s)
