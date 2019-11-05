from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys

def getTitle(url):
    try:
        # URL test
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        # Page test
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.ifsul.edu.br")

if title == None:
    print("Título não encontrado")
else:
    print(title)
    
    
