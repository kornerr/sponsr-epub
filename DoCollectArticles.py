import time
from constants import *
from entities import *
from other import *

class DoCollectArticles:
    def __init__(self, fileCache):
        self.fileCache = fileCache
        self.drv = None
        self.out = []

    def execute(self):
        service = Service(
            executable_path = SELENIUM_DRIVER,
            service_args = ["--marionette-port", "2828", "--connect-existing"]
        )
        self.drv = webdriver.Firefox(service = service)

        url = BASE_URL + FIRST_POST
        lines = readFileLines(self.fileCache)
#        if not lines.isEmpty:
#            url = 
        counter = 0
        while counter < VISIT_LIMIT:
            print("ИГР counter:", counter)
            a = self.loadArticle(url)
            self.print(str(a))
            url = BASE_URL + a.nextId
            counter += 1
            time.sleep(3)
        lines += self.out
        writeFileLines(self.fileCache, lines)

    def loadArticle(self, url):
        print("01")
        html = webPageHTML(self.drv, url)
        print("02")
        a = Article()
        a.date = parseArticleDate(html)
        a.id = parseArticleId(html)
        a.nextId = parseArticleNextId(html)
        a.text = parseArticleText(html)
        a.title = parseArticleTitle(html)
        return a

    def print(self, s):
        self.out.append(s)
        print(s)

