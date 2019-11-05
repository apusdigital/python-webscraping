from urllib.request import urlopen
from bs4 import BeautifulSoup

# Retrieve HTML string from the URL
html = urlopen("http://www.ifsul.edu.br")

# Create BeautifulSoup Object
bsObj = BeautifulSoup(html, "html.parser")

# Print first h1 reader
print(bsObj.h1)
