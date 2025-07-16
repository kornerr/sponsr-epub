from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
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

        a = self.loadPage(FIRST_POST, True)
        self.print(a)

    def loadPage(self, url, reload):
        # Reload the page
        if reload:
            self.drv.get(url)
        a = Article()
        html = self.drv.page_source
        a.src = html
        a.date = parseArticleDate(html)

        return a

    def print(self, s):
        self.out.append(s)
        print(s)

