# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

cores = {'fim':'\033[m',
         'nverm':'\033[1;31m',
         'nverd':'\033[1;32m',
         'ncia':'\033[1;36m'}
         
from datetime import date

ano = int(input('Informe o seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano

if idade == 18:
    print('{}Já está na hora de você se alistar!{}'.format(cores['nverd'], cores['fim']))
elif idade < 18:
    print('Ainda faltam {} anos para você se alistar!'.format(18-idade))
    print('Seu alistamento será em {}{}{}.'.format(cores['ncia'], atual+(18-idade), cores['fim']))
else:
    print('Você já deveria ter se alistado há {} anos!'.format(idade-18))
    print('Seu alistamento foi em {}{}{}.'.format(cores['nverm'], atual-(idade-18), cores['fim']))
