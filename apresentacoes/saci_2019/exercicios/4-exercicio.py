import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://intranet.ifsul.edu.br/catalogo/campus/2")
bsObj = BeautifulSoup(html, "html.parser")
	
lista = bsObj.select("a[href*=http://intranet.ifsul.edu.br/catalogo/curso/]")

arquivo = csv.writer(open("4-exercicio.csv", "w"))

for cursos in lista:
	arquivo.writerow([cursos.get_text()])
	
arquivo = open("4-exercicio.txt","w+")

for cursos in lista:
	 arquivo.write(cursos.get_text()+"\n")			


