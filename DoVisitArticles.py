from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
import time

from constants import *
from other import *

class DoVisitArticles:
    def __init__(self):
        self.drv = None

    def execute(self):
        service = Service(
            executable_path = SELENIUM_DRIVER,
            service_args = ["--marionette-port", "2828", "--connect-existing"]
        )
        self.drv = webdriver.Firefox(service = service)
        self.printPage(FIRST_POST)

    def printPage(self, url):
        # Load the page
        self.drv.get(url)
        # Get page URL
        print("URL", self.drv.current_url)
        # Get page source
        html = self.drv.page_source
        dt = pageDate(html)
        print("DATE", dt)
