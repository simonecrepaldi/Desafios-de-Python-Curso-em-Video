# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

cores = {'fim':'\033[m',
         'mag':'\033[1;35m'}

a = int(input('Digite um número inteiro qualquer: '))
b = int = int(input('Digite um outro número inteiro qualquer: '))

if a == b:
    print('Não existe valor maior, {}os dois valores são iguais{}|'.format(cores['mag'], cores['fim']))
elif a > b:
    print('O {}primeiro{} valor é maior!'.format(cores['mag'], cores['fim']))
else:
    print('O {}segundo{} valor é maior!'.format(cores['mag'], cores['fim']))
