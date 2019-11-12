'''
Task: 

Tendo como ponto de partida o endereço: https://portal.ufpel.edu.br

5. Armazene o conteúdo da questão anterior no formato "txt". 

Solution:
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://portal.ufpel.edu.br")
bsObj = BeautifulSoup(html, "html.parser")
	
lista = bsObj.findAll("div", {"class":"menu-servicos-container"})

arquivo = open("output.txt","w+")

for item in lista:
    arquivo.write(item.get_text()+"\n")	