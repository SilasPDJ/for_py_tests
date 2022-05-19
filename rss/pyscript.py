import subprocess
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# continuar a desenvolver a def real_path, p/ driver
from webdriver_manager.chrome import ChromeDriverManager

link = "Chromedriver/chromedriver.exe"
this_file_path = os.path.realpath(__file__)
path = os.path.dirname(this_file_path)
link = os.path.join(path, link)

SERVICE = Service(ChromeDriverManager().install())
# procura link chamado pela variável __file__


def pgdas_driver(path=''):
    """
    :param path: default path atual
    :return: o driver para fechar no loop
    """

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--verbose')
    # profile chrome_options.add_argument("user-data-dir=C:\\Users\\AtechM_03\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": True,
        'profile.default_content_setting_values.automatic_downloads': 1

    })

    chromedriver = link
    # real_path_for_chromedriver()
    # vindo do ginfess_driver [magic]
    driver = webdriver.Chrome(
        service=SERVICE, options=chrome_options)
    return driver


client_path = r"O:\OneDrive\_FISCAL-2021\2022\04-2022\Oesk Contabil"

driver = pgdas_driver(client_path)
driver.get(
    "https://www8.receita.fazenda.gov.br/SimplesNacional/controleAcesso/Autentica.aspx?id=60")
# data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALQAAAAyCAYAAAD1JPH3AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAABb2SURBVHhe7d1brHbT1QdwkZZGGqeizoemRWhLEZEXLRGHliLOhzpHEMcilB6cTyH1VYi8RIiIirQVQcQhEZoSXDh8F7j59L3iztUXF9/F872/9b7jydhzz7nWevZ+aC/6T0b23mvNOeaY4zTHnGs9z15n0003/e911llnUtI3vvGN/9tggw3+d+ONN/5il112+Z8VK1a8j4466qh/XHPNNc+sXLnysaCXX375/slkcmONVq1adWfQW2+9dW+tzX/o35vefPPN/8o2DnvmNvMifPnUUvmvs9VWW31ec+ivm7bccsvJQQcdNKUjjjhicsMNN0z+/Oc/T1YHwmpZ1+C1116bfPnll2v/Wogvvvhi8tlnn03ee++9BX3G4O2335488MADHX98MoxXXpsH8DVebcw+aDu2zz//+c+OWsCjjw9dho2eeeaZ6TX0VQBfdg/7zar7dVbTjU8++eQC58q07rrrTlZn6sk3v/nN6v2vi771rW9NDj744O73W265ZY30CSZ97bXXTk466aRpn0cffXTt3X68+OKL0z6/+MUvJq+++uraO2vAkJQ8b3z00UcdX9TnIOaWHbg0eh+eeuqpjloYcs4//OEPU938/Oc/X3v16wFnZuuzzjpr0KnpQvvOof1y7733Tu64447JJ598MrnvvvsmP/rRj6YTCfrud7872XvvvSdHH3305KWXXuqUevLJJ0/vb7vttl2mzX2+Cvr2t7+9IJujffbZpxt/5513nnz/+9+ffO9735sccMABi9rV6Kc//em0zw9+8IPJjjvuuODe9ttv382r5LfnnntW5Vsq4Wc8P5HxfvOb30wuuOCCyc9+9rPmCuLvIYMvFXzj1FNP7WQhoyRBBte/agj4Y445ppt7BJ1xy7mSh2y33377Godec3kxdDSBY489doHi0eraenL22Wd3zn/ddddNHnzwwUWTJJDBUGS5IDyzc+y3336LxvgP9dOuu+7a6e6cc86Z3HTTTb2ZdrlQ+hmTc/sp+X0diBIyUFstQzZJudehMzj3eeedN/nhD3/YLf+h1KCddtqpyyacd1749NNPJ88991wnqJ94n3ba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


capt = "capt.png"

# espera carregar tag com #captcha-img

sleep(5)

driver.execute_script(f"""
let cap = document.querySelector("#captcha-img");
let a = document.createElement("a");
let capSrc = cap.getAttribute("src")
a.setAttribute("href", capSrc);
a.setAttribute("download", "{capt}");
a.click()
""")  # download image

capt_image = os.path.join(client_path, capt)
capt_ready = os.path.join(client_path, "capt_omega.txt")

simplificar = r"Rscript"
subprocess.run(
    f"{simplificar} O:\\HACKING\\MY_PROJECTS\\for_py_tests\\rss\\maintest.R {capt_image.replace(' ', '&&')} {capt_ready.replace(' ', '&&')}"
)

sleep(5)  # vai sleepar mesmo, nao tem jeito
scret = open(capt_ready, "r").read()
input(scret)
os.remove(capt_image)

# -------- ############### O R está funcionando,
# library(decryptr)
# file <- download_captcha("rfb", path = "./img")
# decrypt(file, model = model)
# -----------------

# DESCUBRA COMO INTEGRAR AO SELENIUM E O BRASIL SERÁ DESCOBERTO
