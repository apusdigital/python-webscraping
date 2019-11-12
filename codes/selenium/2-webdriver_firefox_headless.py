from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains

from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(executable_path=r'./geckodriver', options=options)

driver.implicitly_wait(5)
driver.get('https://www.ifsul.edu.br')
driver.get_screenshot_as_file('./ifsul.png')
driver.close()
