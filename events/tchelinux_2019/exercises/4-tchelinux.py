'''
Task: 

Tendo como ponto de partida o endereço: https://www.bage.rs.gov.br

4. Armazene o conteúdo anterior no formato "csv".

Solution:
'''

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.bage.rs.gov.br/index.php/estrutura-administrativa/secretarias/")
bsObj = BeautifulSoup(html, "html.parser")

# busca o conteúdo de uma classe dentro de uma div	
lista = bsObj.findAll("div", {"class":"entry-content"})
# remove as tags html
lista = lista[0].get_text()
# separa as seções com base no padrão escrito no html
lista = (str(lista).split('__________________________________________________________________________________'))
# cria o arquivo csv
arquivo = csv.writer(open("4-tchelinux.csv", "w"))
# percorre a lista e grava as linhas no arquivo
for secretarias in lista:
	arquivo.writerow([secretarias])
	
		


