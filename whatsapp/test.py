from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
from webdriver_manager.chrome import ChromeDriverManager  # 1st changer
from wbs import WDShorcuts


def banner():
    print('''
		  ##              ##  =======     ####       ####    ####     =======
		  \ \    ####    / /  #      #  ##    ##    / /\ \  / /\ \    #      #
		   \ \  / /\ \  / /   #======   ##    ##   / /  \ \/ /  \ \   #====== 
		    \ \/ /  \ \/ /    #      #  ##    ##  / /    ####    \ \  #      #
		     ####    ####     =======     ####    ##              ##  =======
		''')


def create_driver():
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium import webdriver

    profile_path = r'C:\Users\silas\AppData\Roaming\Mozilla\Firefox\Profiles\mf8yrvyy.default-release'

    options = webdriver.FirefoxOptions()
    options.set_preference("profile", profile_path)
    options.add_argument('-profile')
    options.add_argument(profile_path)

    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(
        service=service, options=options)
    return driver


def main():
    driver.get('https://web.whatsapp.com/')
    driver.maximize_window()
    # name = input('Enter the name of usser or group: ')
    name = 'Silas sala'
    msg = input('Enter your message: ')
    count = int(input('Enter the count: '))

    input('Enter any key after scanning QR code')
    sleep(3)
    user = driver.find_element(By.XPATH, '//span[@title = "{}"]'.format(name))
    user.click()

    # The classname of message box may vary.

    for i in range(count):
        ddriver.send_keys_anywhere(msg)
        input("hi")
        # The classname of send button may vary.
        button = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
        button.click()
    print('Bombing Complete!!')


driver = create_driver()
ddriver = WDShorcuts(driver)

banner()
main()
