# Exemplo de uma API de dados

from urllib.request import urlopen
import json

# Busca as escolas brasileiras que operam sem: energia, água e esgoto
busca = urlopen('http://educacao.dadosabertosbr.com/api/escolas/buscaavancada?situacaoFuncionamento=1&energiaInexistente=on&aguaInexistente=on&esgotoInexistente=on')

# Carrega o json
res = json.loads(busca.read().decode('utf-8'))

print('Total:', res[0])

for e in res[1]:
    print(e['nome'])
    print(e['estado'], e['regiao'])
