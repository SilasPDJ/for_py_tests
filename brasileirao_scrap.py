from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import pandas as pd

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


def webdriverwait(by: By.ID, el: str): return WebDriverWait(
    driver, 30).until(ec.presence_of_element_located((by, el)))


def send_keys_anywhere(*keys, p=0.13):
    a = ActionChains(driver)
    for key in keys:
        a.send_keys(key)
        a.pause(p)
    a.perform()


driver.get('https://www.google.com/')
send_keys_anywhere('Brasileirão', Keys.ENTER)

# driver.find_element_by_css_selector('[aria-label=Ver mais]')

# ver_mais = WebDriverWait(driver, 30).until(
#     ec.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Ver mais"]')))
ver_mais = webdriverwait(By.CSS_SELECTOR, '[aria-label="Ver mais"]')

ver_mais.click()

webdriverwait(By.TAG_NAME, 'body')

sleep(2)
driver.find_elements(By.TAG_NAME, 'li')[4].click()


sleep(2)
html = driver.find_element(By.CSS_SELECTOR,
                           "#tab-1-3 > div > div.imso-ani.tb_cbg > div").get_attribute('outerHTML')

soup = BeautifulSoup(html, 'html.parser')
table = soup.find(name='table')

table = str(table)

a = pd.read_html(table)[0]
# a = pd.read_html(soup)

# outerHTML x innerHTML

input(a)
