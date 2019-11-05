'''
Task: 

Tendo como ponto de partida o endereço: https://portal.ufpel.edu.br

1. Mostre o trecho que exibe o Copyright do portal.

Solution:
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://portal.ufpel.edu.br")
bsObj = BeautifulSoup(html, "html.parser")

lista = bsObj.findAll("div", {"id":"creditos"})
print(lista[0].get_text())


