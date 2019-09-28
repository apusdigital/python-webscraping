
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://intranet.ifsul.edu.br/catalogo/campus/2")
bsObj = BeautifulSoup(html, "html.parser")
	
lista = bsObj.select("a[href*=http://intranet.ifsul.edu.br/catalogo/curso/]")

for cursos in lista:
	print(cursos.get_text())	


'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://intranet.ifsul.edu.br/catalogo/campus/2")
bsObj = BeautifulSoup(html, "html.parser")

# busca tudo o que está dentro da div com class "tile-collection"
for child in bsObj.find("div",{"class":"tile-collection"}):
	bsObj.find("div",{"class":"tile-collection"})
	#print(child)
'''
