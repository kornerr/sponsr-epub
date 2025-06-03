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
        service = Service(
            executable_path = "/Volumes/MOE/bin/geckodriver",
            service_args = ["--marionette-port", "2828", "--connect-existing"]
        )
        drv = webdriver.Firefox(service = service)
        drv.get(FIRST_POST)
        items = drv.find_elements(By.CSS_SELECTOR, CSS_PICKER)
        # Use the first date picker, the second one is something wrong.
        picker = items[0]
        d = countedDays(picker)
        print(d)
