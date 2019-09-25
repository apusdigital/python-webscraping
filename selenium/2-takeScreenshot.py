from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()

driver.implicitly_wait(5)
driver.get('http://www.ifsul.edu.br')
driver.get_screenshot_as_file('./pythonscraping.png')
driver.close()
