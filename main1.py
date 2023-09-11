import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
import os
import numpy as np
import time

"""# Configuração do Web-Driver"""

# Utilizando o WebDriver do Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instanciando o Objeto ChromeOptions
options = webdriver.ChromeOptions()


# Passando algumas opções para esse ChromeOptions
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--start-maximized')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-crash-reporter')
options.add_argument('--log-level=3')

# Criação do WebDriver do Chrome
wd_Chrome = webdriver.Chrome('chromedriver',options=options)

# abrir a pagina flashscore

wd_Chrome.get("https://www.flashscore.com/")
time.sleep(2)

#pegar a data de hoje

date = wd_Chrome.find_element(By.CSS_SELECTOR, 'button#calendarMenu').text
print(date)

#primeiro jogo ao vivo
live = wd_Chrome.find_element(By.CSS_SELECTOR, 'div.event__match--live')
casa =live.find_element(By.CSS_SELECTOR, 'div.event__participant--home').text
fora =live.find_element(By.CSS_SELECTOR, 'div.event__participant--away').text
print(f'{casa} x {fora}')

#pegar todos os jogos de hoje

todos = wd_Chrome.find_elements(By.CSS_SELECTOR, 'div.event__match--live')
for jogo in todos:
    casa =jogo.find_element(By.CSS_SELECTOR, 'div.event__participant--home').text
    fora =jogo.find_element(By.CSS_SELECTOR, 'div.event__participant--away').text
    placar_home = jogo.find_element(By.CSS_SELECTOR, 'div.event__score--home').text
    placar_away = jogo.find_element(By.CSS_SELECTOR, 'div.event__score--away').text
    print(f'{casa} {placar_home} x {placar_away} {fora}')