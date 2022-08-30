# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

# Importando a bilbioteca
import mechanize
br = mechanize.Browser()
url = 'http://pudim.com.br/'

# Programa vai tentar abrir o site
try:
    br.open(url)
# Problema com a conexão
except (ConnectionRefusedError, ConnectionError):
    print('\033[1:31mO site PUDIM não está acessível no momento!\033[m')
# Qualquer outro problema
except Exception as erro:
    print('\033[1:31mO site PUDIM não está acessível no momento!\033[m')
else:
    print('\033[1:32mO site PUDIM está acessível no momento!\033[m')

# Obs: Um mesmo "try" pode ter vários "except"


# Resolvendo o exercício com outra biblioteca
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.UrlError:
    print('O site PUDIM não está acessível no momento.')
else:
    print('Consegui acessar o site PUDIM com sucesso!')
# Mostra o código do site
    print(site.read())
