from urllib.request import urlopen 
from urllib.error import HTTPError
from bs4 import BeautifulSoup
 
try:
    html = urlopen("https://www.python.org/")
 
except HTTPError as e:
    print(e)

else:
    res = BeautifulSoup(html.read(),"html5lib")
    print(res.title)
