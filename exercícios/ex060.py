# Faça um programa que leia um número qualquer e mostre o seu fatorial
# Ex: 5! = 5x4x3x2x1 = 120

print('CALCULANDO O FATORIAL DE UM NÚMERO N')
n = int(input('Digite um número: '))
c = n
fat = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat *= c
    c -= 1
print('{}'.format(fat))

# Solução usando a biblioteca MATH --> FACTORIAL:
from math import factorial
x = int(input('Digite um número: '))
fat = factorial(x)
print('>>> {}! = {}'.format(x, fat))
