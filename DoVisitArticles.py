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
        self.nextId = None

    def execute(self):
        service = Service(
            executable_path = SELENIUM_DRIVER,
            service_args = ["--marionette-port", "2828", "--connect-existing"]
        )
        self.drv = webdriver.Firefox(service = service)
        self.printPage(FIRST_POST)
        self.goToNextArticle()

    def goToNextArticle(self):
        xpath = TEMPLATE_ARTICLE_XPATH.replace("%ARTICLE_ID%", str(self.nextId))
        cell = self.drv.find_element(By.XPATH, xpath)
        cell.click()

    def printPage(self, url):
        # Load the page
        self.drv.get(url)
        # Get page source
        html = self.drv.page_source
        dt = pageDate(html)
        # Locate picker
        items = self.drv.find_elements(By.CSS_SELECTOR, CSS_PICKER)

        # Reload the page to re-locate the missing picker
        if (len(items) < 2):
            self.printPage(url)
            return

        print("URL", self.drv.current_url)
        print("DATE", dt)

        # Use the second date picker, the reason is unclear.
        picker = items[1]
        cd = countedDays(picker)
        self.nextId = nextArticleId(cd, dt)
