import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.ifsul.edu.br")
bsObj = BeautifulSoup(html, "html.parser")

# Create output file
arquivo = open("output.txt","w+")

# Select content by CSS class
nameList = bsObj.findAll("div", {"class":"tile-collection"})

for name in nameList:
    arquivo.write(name.get_text()+"\n")	

	 
