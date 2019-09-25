from urllib.request import urlopen
from bs4 import BeautifulSoup
 
html = urlopen("https://www.python.org/")
res = BeautifulSoup(html.read(),"html5lib");
print(res.title)
