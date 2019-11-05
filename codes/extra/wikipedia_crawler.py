# Exemplo de um web crawler (rastreador web)

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

# Gera pseudo-random números
random.seed(datetime.datetime.now())

# Função que navega entre os links
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

# Define o ponto de partida
links = getLinks("/wiki/Web_scraping")

# Enquanto houverem links, mostra as URLs
while len(links) > 0:
    newArticle = random.choice(links).attrs["href"] 
    print(newArticle)
    links = getLinks(newArticle)
