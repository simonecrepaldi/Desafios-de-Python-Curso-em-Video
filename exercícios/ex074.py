# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

print('\033[1;35mPrimeira forma de resolver\033[m')
from random import randint
# Criando uma tupla com 5 valores sorteados entre 0 e 10
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

print('')

print('\033[1;35mSegunda forma de resolver\033[m')
from random import sample
# Criando a tupla "num" com 5 elementos e depois colocando em ordem (sorted)
num = tuple(sample(range(1000), 5))
print(f'Os números gerados foram {sorted(num)}')
print(f'Maior número da tupla: {max(num)}')
print(f'Menor número da tupla: {min(num)}')

print('')

print('\033[1;35mTerceira forma de resolver\033[m')
from random import randint
lista = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
# Colocando os valores em ordem crescente e depois selecionando a posição 0 (menor valor) e a posição 4 (maior valor)
organizado = (sorted(lista))
print(f'→ Os números gerados foram: {lista}.')
print(f'→ O maior número foi {organizado[4]}.')
print(f'→ O menor número foi {organizado[0]}.')
