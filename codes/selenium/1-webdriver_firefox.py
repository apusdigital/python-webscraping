from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Load webdriver (GUI mode)
driver = webdriver.Firefox(executable_path=r'./geckodriver')

# Get page
driver.get('http://www.ifsul.edu.br')


  



