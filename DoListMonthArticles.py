from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
import time

from constants import *
from other import *

# Output: ?
class DoListMonthArticles:
    def __init__(self):
        self.variable = False

    def execute(self):
        self.service = Service(
            executable_path = "/Volumes/MOE/bin/geckodriver",
            service_args = ["--marionette-port", "2828", "--connect-existing"]
        )
        self.drv = webdriver.Firefox(service = self.service)
        self.drv.get(FIRST_POST)
        counter = 0
        while counter < 2:
            nextId = self.printPageMap()
            self.goToMonth(nextId)
            counter += 1
            time.sleep(5)

    def goToMonth(self, id):
        xpath = TEMPLATE_ARTICLE_XPATH.replace("%ARTICLE_ID%", str(id))
        cell = self.drv.find_element(By.XPATH, xpath)
        cell.click()

    def printPageMap(self):
        print("PAGE_URL", self.drv.current_url)
        items = self.drv.find_elements(By.CSS_SELECTOR, CSS_PICKER)
        # Use the first date picker, the second one is broken.
        picker = items[0]
        cd = countedDays(picker)
        ppm = countPagesPerMonth(cd)
        monthNow = detectCurrentMonth(ppm)
        print("NOW", monthNow)
        monthNext = detectNextMonth(ppm, monthNow)
        print("NEXT", monthNext)
        nextMonthArticleId = list(cd.keys())[-1]
        print("NEXT_ARTICLE_ID", nextMonthArticleId)
        for id in cd:
            mo = cd[id]
            print("CAL", id, mo)
        return nextMonthArticleId
