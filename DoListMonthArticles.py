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
        url = FIRST_POST

        # Load the page
        self.drv.get(url)
        print("URL", self.drv.current_url)

        # Get its source code
        html = self.drv.page_source
        lines = html.split("\n")
        isDate = False
        for ln in lines:
            # Parse date
            if isDate:
                isDate = False
                lnt = ln.strip()
                parts = lnt.split(" ")
                inverseDt = parts[0]
                dps = inverseDt.split(".")
                print(f"DATE {dps[2]}-{int(dps[1])}-{int(dps[0])}")
            # Find date marker
            if ARTICLE_DATE_MARKER in ln:
                isDate = True

        items = self.drv.find_elements(By.CSS_SELECTOR, CSS_PICKER)
        # Use the second date picker, the reason is unclear.
        picker = items[1]
        cd = countedDays(picker)
        print(cd)

    def goToMonth(self, id):
#        xpath = TEMPLATE_ARTICLE_XPATH.replace("%ARTICLE_ID%", str(id))
#        cell = self.drv.find_element(By.XPATH, xpath)
#        cell.click()
        nextMonth = self.drv.find_element(By.XPATH, XPATH_NEXT_MONTH)
        nextMonth.click()

    def printPageMap(self):
        print("PAGE_URL", self.drv.current_url)
        items = self.drv.find_elements(By.CSS_SELECTOR, CSS_PICKER)
        # Use the second date picker, the reason is unclear.
        picker = items[1]
        cd = countedDays(picker)
        ppm = countPagesPerMonth(cd)
        monthNow = detectCurrentMonth(ppm)
        print("NOW", monthNow)
        monthNext = detectNextMonth(ppm, monthNow)
        print("NEXT", monthNext)
        nextMonthArticleId = list(cd.keys())[-1]
        print("NEXT_ARTICLE_ID", nextMonthArticleId)
        print(cd)
        for id in cd:
            mo = cd[id]
            #print("CAL", id, mo)
        return nextMonthArticleId
