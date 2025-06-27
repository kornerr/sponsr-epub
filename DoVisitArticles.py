from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
import time

from constants import *
from other import *

class DoVisitArticles:
    def __init__(self):
        pass

    def execute(self):
        service = Service(
            executable_path = SELENIUM_DRIVER,
            service_args = ["--marionette-port", "2828", "--connect-existing"]
        )
        drv = webdriver.Firefox(service = service)
        url = FIRST_POST

        # Load the page
        drv.get(url)

        # Get page URL
        print("URL", drv.current_url)

        # Get page source
        html = drv.page_source

        dt = pageDate(html)
        print("DATE", dt)
