from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium import webdriver

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
        self.printPageMap()

    def printPageMap(self):
        print(self.drv.current_url)
        items = self.drv.find_elements(By.CSS_SELECTOR, CSS_PICKER)
        # Use the first date picker, the second one is broken.
        picker = items[0]
        cd = countedDays(picker)
        print(cd)
        ppm = countPagesPerMonth(cd)
        monthNow = detectCurrentMonth(ppm)
        print(monthNow)
        monthNext = detectNextMonth(ppm, monthNow)
        print(monthNext)
