'''
Task: 

Tendo como ponto de partida o endereço: https://portal.ufpel.edu.br

4. Faça uma extração da lista de serviços disponíveis na UFPEL.

Solution:
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://portal.ufpel.edu.br")
bsObj = BeautifulSoup(html, "html.parser")
	
lista = bsObj.findAll("div", {"class":"menu-servicos-container"})
print(lista[0].get_text())