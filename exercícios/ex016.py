# Crie um programa que leia um número real pelo teclado e mostre na tela a sua posição inteira.
# Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

#Importando a biblioteca math
from math import trunc

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua parte inteira é {}!'.format(num, trunc(num)))
print('='*35)
print('Outra maneira de resolver o exercício, sem usar a biblioteca math')


# Uma outra maneira de fazer, sem precisar importar a biblioteca math:
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}!'.format(num, int(num)))
