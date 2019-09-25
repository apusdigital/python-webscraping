from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.ifsul.edu.br")
bsObj = BeautifulSoup(html, "html.parser")

# busca tudo o que está dentro da div com class "tile-collection"
for child in bsObj.find("div",{"class":"tile-collection"}).children:
    print(child)
