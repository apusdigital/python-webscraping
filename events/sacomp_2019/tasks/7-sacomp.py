'''
Task: 

Tendo como ponto de partida o endereço: https://portal.ufpel.edu.br

7.  Salve  uma  captura  da  tela  principal  do  portal  com  nome  de "ufpel_website.png".

Solution:
'''

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains

from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(executable_path=r'./geckodriver', options=options)

driver.implicitly_wait(5)
driver.get('https://portal.ufpel.edu.br')
driver.get_screenshot_as_file('./ufpel_website.png')
driver.close()
