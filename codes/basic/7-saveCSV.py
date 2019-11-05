import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.ifsul.edu.br")
bsObj = BeautifulSoup(html, "html.parser")

# Create output file
arquivo = csv.writer(open("output.csv", "w"))

# Select content by CSS class
nameList = bsObj.findAll("div", {"class":"tile-collection"})

for name in nameList:
    arquivo.writerow(name.get_text()+"\n")	

