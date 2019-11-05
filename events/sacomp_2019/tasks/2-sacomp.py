'''
Task: 

Tendo como ponto de partida o endereço: https://portal.ufpel.edu.br

2. Exiba os informes acadêmicos mostrados na página inicial.

Solution:
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://ccs2.ufpel.edu.br/wp/category/noticias/")
bsObj = BeautifulSoup(html, "html.parser")
	
lista = bsObj.findAll("ul", {"id":"search_bloco"})
print(lista[0].get_text())	
