'''
Task: 

Tendo como ponto de partida o endereço: https://www.bage.rs.gov.br

2. Exiba as últimas notícias da página inicial (sem as tags HTML).

Solution:
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.bage.rs.gov.br/")
bsObj = BeautifulSoup(html, "html.parser")
	
lista = bsObj.findAll("section", {"id":"lp-boxes-2"})
print(lista[0].get_text())	
