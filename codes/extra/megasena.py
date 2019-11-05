# Retorna os dados da Megasena

import requests
from bs4 import BeautifulSoup as bs

# Url do resultado
url = 'http://www1.caixa.gov.br/loterias/loterias/megasena/megasena_pesquisa_new.asp'
# Salva a página
req = requests.get(url)

# Cria o objeto BeautifulSoap
bsObj = bs(req.content, 'html.parser')

lista = bsObj.find('ul')
numeros = lista.findAll('li')

for n in numeros: 
	print (n.getText())
    
