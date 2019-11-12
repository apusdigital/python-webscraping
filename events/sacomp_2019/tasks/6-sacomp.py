'''
Task: 

Tendo como ponto de partida o endereço: https://portal.ufpel.edu.br

6.  Considerando  a  mesma  lista  de  serviços  crie  um  arquivo  CSV com o seguinte cabeçalho e conteúdo: Serviço; Link 

Solution:
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

html = urlopen("https://portal.ufpel.edu.br")
bsObj = BeautifulSoup(html, "html.parser")

# cria o arquivo
arquivo = csv.writer(open("output.csv","w+"), delimiter =";", quoting=csv.QUOTE_MINIMAL) 
# escreve o cabeçalho
arquivo.writerow(['Serviço', 'Link'])
# escreve as linhas
for data in bsObj.find_all("div", {"class":"menu-servicos-container"}):
    for a in data.find_all('a'):
        arquivo.writerow([a.text, a.get('href')])


