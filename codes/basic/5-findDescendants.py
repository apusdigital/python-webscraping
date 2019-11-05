from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.ifsul.edu.br")
bsObj = BeautifulSoup(html, "html.parser")

# Find all content in CSS class "tile-collection"
for child in bsObj.find("div",{"class":"tile-collection"}).children:
    print(child)
