from ast import parse
from functools import partial
from time import sleep
import requests
import bs4
import pyautogui as pygui
from pyautogui import Window
from pyperclip import copy, paste


def ativa_janela(p: Window):
    """
    :param p: py32win
    """
    # ativa qualquer janela
    p.restore()
    p.show()
    p.activate()
    pygui.click(p.center, clicks=0)


def send_write(txt: str):
    copy(txt)
    pygui.hotkey('ctrl', 'v')
    sleep(1)
    pygui.hotkey('enter')
    sleep(2)


url = "https://pt.wikipedia.org/wiki/Pol%C3%ADcia"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
response = requests.get(url, headers=headers)

soup = bs4.BeautifulSoup(response.content, 'html5lib')
# r.text is the content of the response in Unicode, and r.content is the content of the response in bytes.
el = soup.find(class_='mw-parser-output')
maxaccept = 'klçkdçaskfdasçlfskaçlfasklçsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
maxaccept = len(maxaccept)

ativa_janela(pygui.getWindowsWithTitle('Habbo BR |')[0])


for p in el.find_all('p'):
    txt = p.get_text()

    calc_div_accpt = len(txt) / maxaccept
    if calc_div_accpt > 1.0:
        contwrite = 0
        #
        rangedcalc = int(calc_div_accpt)+1
        ranged = partial(range, rangedcalc)
        #
        printed_maxlen = txt[:maxaccept].rfind(' ')
        for i in ranged():

            send_write(txt[contwrite:printed_maxlen])

            print(contwrite, printed_maxlen)
            contwrite += printed_maxlen
            printed_maxlen += contwrite

            if printed_maxlen > len(txt):
                printed_maxlen = len(txt)

    else:
        send_write(txt)
