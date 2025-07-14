from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
import time

from constants import *
from other import *

class DoVisitArticles:
    def __init__(self, fileCache):
        self.fileCache = fileCache
        self.drv = None
        self.nextId = None
        self.out = []

    def execute(self):
        service = Service(
            executable_path = SELENIUM_DRIVER,
            service_args = ["--marionette-port", "2828", "--connect-existing"]
        )
        self.drv = webdriver.Firefox(service = service)

        self.nextId = self.printPage(FIRST_POST, True)
        for i in range(0, VISIT_LIMIT):
            ok = False
            while not ok:
                ok = self.goToNextArticleByDay()
                if not ok:
                    self.nextId = self.goToNextArticleByMonth()
            self.nextId = self.printPage(self.drv.current_url, False)
            time.sleep(3)
        writeFileLines(self.fileCache, self.out)

    def goToNextArticleByDay(self):
        xpath = TEMPLATE_ARTICLE_XPATH.replace("%ARTICLE_ID%", str(self.nextId))
        try:
            cell = self.drv.find_element(By.XPATH, xpath)
            cell.click()
            return True
        except Exception as err:
            print(err)
            return False

    def goToNextArticleByMonth(self):
        xpath = XPATH_NEXT_MONTH
        try:
            cell = self.drv.find_element(By.XPATH, xpath)
            cell.click()
            return 1
        except Exception as err:
            print(err)
            return 0

    def print(self, s):
        self.out.append(s)
        print(s)

    def printPage(self, url, reload):
        # Reload the page
        if reload:
            self.drv.get(url)
        # Get page source
        html = self.drv.page_source
        dt = pageDate(html)
        # Locate picker
        items = self.drv.find_elements(By.CSS_SELECTOR, CSS_PICKER)

        # Reload the page to re-locate the missing picker
        if (len(items) < 2):
            return self.printPage(url, True)

        # Use the second date picker, the reason is unclear.
        picker = items[1]
        cd = countedDays(picker)

        self.print(ARTICLE_PREFIX_URL + self.drv.current_url)
        self.print(ARTICLE_PREFIX_DATE + dt)
        self.print(ARTICLE_PREFIX_SRC + html)

        return nextArticleId(cd, dt)
