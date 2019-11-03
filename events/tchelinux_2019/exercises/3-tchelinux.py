'''
Task: 

Tendo como ponto de partida o endereço: https://www.bage.rs.gov.br/index.php/estrutura-administrativa/secretarias/

3. Faça uma extração das secretarias que compõem a gestão municipal atual.

Solution:
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.bage.rs.gov.br/index.php/estrutura-administrativa/secretarias/")
bsObj = BeautifulSoup(html, "html.parser")
	
lista = bsObj.findAll("div", {"class":"entry-content"})

for secretarias in lista:
	print(secretarias.get_text())	
