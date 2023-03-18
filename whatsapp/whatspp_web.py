from wbs import WDShorcuts
import auto_whatsapp
# my changes (SilasPDJ)
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import os


# Group msg
def get_documents_folder_location():
    """
    :returns: user Documents folder location 
    Author: Silas PDJ
    """
    from platform import system
    import win32com
    import pythoncom
    if system() == 'Windows':
        pythoncom.CoInitialize()
        shell = win32com.client.Dispatch("WScript.Shell")
        my_documents = shell.SpecialFolders("MyDocuments")
        # print(my_documents)
    else:
        my_documents = os.path.expanduser("~/Documents")
    return my_documents


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


# pip install auto_whatsapp
msg = '''
Por gentileza, Smart Surf Modas 777 LTDA!
Seguem anexados:
-> DAS sobre faturamento de R$ SEM VALOR A PAGAR 
-> Protocolos e demonstrativos respectivos 
NÃO há boleto a pagar.
________________________________________
Este e-mail é automático. Considerar sempre o e-mail mais atual.
Por gentileza, cheque o nome e o CNPJ (07083804000140) 
Caso haja qualquer conflito, responda sem hesitar esta mensagem neste e-mail.
Todas as declarações são e continuarão sendo feitas minuciosamente.
ATT, Oesk Contábil
'''.strip()

mensagens = [msg, ":-)", ":-*", "<3"]

# users = ["Mãe", "Pai", "+91 9876543210"]
users = ["Silas sala"]

driver = create_driver()
ddriver = WDShorcuts(driver)

driver.get('https://web.whatsapp.com/')
auto_whatsapp.sendChat(users, mensagens, driver)
# path = r"O:\OneDrive\Imagens\cerri5.png"
path = r"O:\OneDrive\_FISCAL-2021\2023\01-2023\Smart Surf Modas 777 LTDA\PGDASD-DECLARACAO-07083804202301001.pdf"
auto_whatsapp.sendMedia(users, path, driver)
# auto_whatsapp.sendChat(users, msg, driver)
