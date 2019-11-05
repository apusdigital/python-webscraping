from urllib.request import urlopen 

# Retrieve HTML string from the URL
html = urlopen("http://www.ifsul.edu.br")

print(html.read())
