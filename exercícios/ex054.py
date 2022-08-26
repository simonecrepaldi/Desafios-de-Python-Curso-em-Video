# Crie um programa que leia o ano de nascimento de sete pessoas
# No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores (21 anos)

from datetime import date

atual = date.today().year
maior = 0
menor = 0

for pessoas in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pessoas)))
    idade = atual - ano
    if idade>= 21:
        maior += 1
    else:
        menor += 1
print('Total de pessoas que já atingiram a maioridade: {}'.format(maior))
print('Total de pessoas que ainda não atingiram a maioridade: {}'.format(menor))
