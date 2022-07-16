from pyautogui import hotkey
from time import time, sleep
from my_record import my_record_audio as mra
from functools import partial
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, JavascriptException

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

from selenium.webdriver.chrome.options import Options


def get_driver():
    chrome_options = Options()

    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": 'O:\\HACKING\\MY_PROJECTS\\for_py_tests\\my_record',

    })

    # #############
    chrome_options.add_extension(
        "extentions/1.1.2_0.crx")

    # funfou o folder dentro dele..........
    # chrome://extensions/ FEZ TUDO

    # service = Service(GeckoDriverManager().install())
    # driver = webdriver.Firefox(service=service)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_window_position(-1300, 10)
    return driver


driver = get_driver()


def send_keys_anywhere(typed, times=1, pause=.13):
    """
    :param typed: o que quero digitar EM QUALQUER LUGAR DO NAVEGADOR
    :param pause: float interval
    :param times: quantidade de vezes
    :return: já digitado
    """
    from time import sleep

    actions = ActionChains(driver=driver)
    for i in range(times):
        # print('send keys')
        actions.send_keys(typed)
        actions.pause(pause)
    actions.perform()
    sleep(1)


def tag_with_text(tag, searched):
    td_tag = driver.find_element(By.XPATH,
                                 f"//{tag}[contains(text(),'{searched.rstrip()}')]")
    return td_tag


def change_save_format():
    driver.get('chrome-extension://kfokdmfpdnokpmpbjhjbcabgligoelgp/options.html')

    tag_with_text('label', '.wav').click()

    sleep(1)
    hardel = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(
        (By.ID, 'save')))

    hardel.click()
    sleep(3)


def record_audio(start=True):
    if start:
        hotkey('ctrl', 'shift', 's')
    else:
        sleep(7)
        hotkey('ctrl', 'shift', 'x')


def click_ac_elementors(*args, pause=1.5):
    """
    :param args: element already defined
    :param pause: pause between clicks and elements
    :return:
    """
    action = ActionChains(driver=driver)
    for arg in args:
        action.move_to_element(arg)
        action.click()
    # x, y = xy = driver.find_element(By.TAG_NAME, 'label').location.values()
    action.perform()
    driver.implicitly_wait(pause)


def __tocar_som():
    import pyautogui as pygui
    pygui.hotkey('ctrl', 'shift', 'j')
    sleep(1)
    pygui.write('tocar_som()')
    sleep(3)
    pygui.hotkey('enter')
    sleep(1)
    pygui.hotkey('ctrl', 'shift', 'j')


get_captcha_token = partial(driver.execute_script,
                            "console.log(getCookie('captcha_token'))")

change_save_format()

driver.get(
    "https://www8.receita.fazenda.gov.br/SimplesNacional/controleAcesso/Autentica.aspx?id=60")
# base_url + sound_folder + token + '.wav';

driver.implicitly_wait(30)
cod_caract = driver.find_element(By.ID,
                                 'txtTexto_captcha_serpro_gov_br')
driver.implicitly_wait(30)


record_audio()
__tocar_som()
# driver.find_element(By.ID, 'btnTocarSom_captcha_serpro_gov_br').click()
sleep(2)
record_audio(False)
driver.switch_to.window(driver.window_handles[1])

hardel = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(
    (By.ID, 'saveCapture')))

hardel.click()
driver.switch_to.window(driver.window_handles[0])


cod_caract.click()

# ctrl shift + s, x

# cod_caract.click()
driver.execute_script('console.log(base_url)')
driver.execute_script('console.log(sound_folder)')
# driver.execute_script('console.log(token)')
driver.execute_script('console.log(".wav")')
sleep(2)
input('teste')
