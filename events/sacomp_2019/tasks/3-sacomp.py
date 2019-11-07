'''
Task: 

Tendo como ponto de partida o endereço: https://portal.ufpel.edu.br

3. Exiba uma lista contendo as unidades acadêmicas da UFPEL.

Solution:
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://portal.ufpel.edu.br")
bsObj = BeautifulSoup(html, "html.parser")
	
lista = bsObj.findAll("li", {"class":"menu-item-2368"})
print(lista[0].get_text())
