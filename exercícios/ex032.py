# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

# Importando a biblioteca datetime
from datetime import date

ano = int(input('Digite o ano que você deseja analisar (para o ano atual digite 0): '))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(ano))
    