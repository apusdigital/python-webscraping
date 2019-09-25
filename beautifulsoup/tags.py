from urllib.error import HTTPError 
from urllib.error import URLError
from bs4 import BeautifulSoup

html = urlopen("https://www.python.org/")
res = BeautifulSoup(html.read(),"html5lib")
tags = res.findAll("h2", {"class": "widget-title"})
 
for tag in tags:
	print(tag.getText())
