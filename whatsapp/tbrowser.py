from selenium import webdriver
from wbs import WDShorcuts
from webdriver_manager.chrome import ChromeDriverManager  # 1st changer
import os
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def create_tor_driver():
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium import webdriver
    tor_browser_path = r"A:\TOR\Browser\firefox.exe"
    # profile_at = webdriver.FirefoxProfile(
    #     tor_browser_path + '/Browser/TorBrowser/Data/Browser/profile.default')

    service = Service(tor_browser_path)
    driver = webdriver.Firefox(
        service=service)
    return driver


driver = create_tor_driver()
input(driver)
