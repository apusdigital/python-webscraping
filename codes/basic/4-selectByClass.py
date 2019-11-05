from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.ifsul.edu.br")
bsObj = BeautifulSoup(html, "html.parser")

# Select content by CSS class
nameList = bsObj.findAll("div", {"class":"tile-collection"})

for name in nameList:
    print(name.get_text())
