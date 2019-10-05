'''
Task: 

Tendo como ponto de partida o endereço: https://www.bage.rs.gov.br

1. Mostre o Copyright do desenvolvimento do portal.

Solution:
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.bage.rs.gov.br/")
bsObj = BeautifulSoup(html, "html.parser")

lista = bsObj.findAll("section", {"id":"text-5"})
print(lista[0].get_text())


