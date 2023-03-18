#####== SELENIUM BASED WHATSAPP BOT ==#####
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
# pip install -i https://test.pypi.org/simple/ wds-utilities

from wbs import WDShorcuts
# my part


def sendChat(numbers, mensagens: list, driver):
    wait = WebDriverWait(driver, 10)
    ddriver = WDShorcuts(driver)
    sleep(5)

    for i in range(len(numbers)):
        user_arg = '//span[@title=' + '"' + numbers[i] + '"' + '][@dir="auto"]'
        user = wait.until(EC.presence_of_element_located((By.XPATH, user_arg)))
        user.click()
        sleep(4)
        # ddriver.tag_with_text()
        msg_box_arg = '//div[@class="lexical-rich-text-input"]'
        # msg_box = wait.until(
        #     EC.presence_of_element_located((By.XPATH, msg_box_arg)))
        user_arg = '//span[@title=' + '"' + numbers[i] + '"' + '][@dir="auto"]'
        user = wait.until(EC.presence_of_element_located((By.XPATH, user_arg)))
        print("passed")
        user.click()
        sleep(4)
        # msg_box_arg = '//div[@class="lexical-rich-text-input"]'

        # msg_box = wait.until(
        #     EC.presence_of_element_located((By.XPATH, msg_box_arg)))
        msg_box_arg = '//div[@class="lexical-rich-text-input"]'
        # msg_box = ddriver.contains_title(msg_box_arg)
        # msg_box.send_keys(Keys.TAB)
        for msg in mensagens:
            ddriver.send_keys_anywhere(msg)
            ddriver.send_keys_anywhere(Keys.ENTER)
        # msg_box.send_keys(msg + Keys.RETURN)

    sleep(3)
    print('Messages send successfully')
    # driver.quit()


# Send document
def sendDoc(numbers, path, driver):
    wait = WebDriverWait(driver, 300)
    ddriver = WDShorcuts(driver)

    for i in range(len(numbers)):
        user_arg = '//span[@title="' + numbers[i] + '"][@dir="auto"]'
        user = wait.until(EC.presence_of_element_located((By.XPATH, user_arg)))
        user.click()
        sleep(3)

        attach_arg = '//span[@data-testid="clip"]'
        attach = wait.until(
            EC.presence_of_element_located((By.XPATH, attach_arg)))
        attach.click()
        sleep(2)

        doc_box_arg = '//input[@accept="*"][@type="file"]'
        doc_box = wait.until(
            EC.presence_of_element_located((By.XPATH, doc_box_arg)))
        doc_box.send_keys(path)
        sleep(3)

        send_arg = '//span[@data-testid="send"]'
        send = wait.until(EC.presence_of_element_located((By.XPATH, send_arg)))
        send.click()
        sleep(3)

    sleep(5)


# Send media
def sendMedia(numbers, path, driver):
    wait = WebDriverWait(driver, 300)
    ddriver = WDShorcuts(driver)

    for i in range(len(numbers)):
        user_arg = '//span[@title="' + numbers[i] + '"][@dir="auto"]'
        user = wait.until(EC.presence_of_element_located((By.XPATH, user_arg)))
        user.click()
        sleep(3)

        attach_arg = '//span[@data-testid="clip"]'
        attach = wait.until(
            EC.presence_of_element_located((By.XPATH, attach_arg)))
        attach.click()
        sleep(2)

        doc_box_arg = '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"][@type="file"]'
        doc_box = wait.until(
            EC.presence_of_element_located((By.XPATH, doc_box_arg)))
        doc_box.send_keys(path)
        sleep(5)

        send_arg = '//span[@data-testid="send"]'
        send = wait.until(EC.presence_of_element_located((By.XPATH, send_arg)))
        send.click()
        sleep(3)

    sleep(5)
