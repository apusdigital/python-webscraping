from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.ifsul.edu.br")
bsObj = BeautifulSoup(html, "html.parser")

lista = bsObj.findAll("div", {"class":"footer-ferramenta"})
print(lista[0].get_text())


