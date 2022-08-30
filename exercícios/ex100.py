# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

# Importando as bibliotecas
from random import randint
from time import sleep

# Definindo a função "sorteia"
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
# Fazendo o programa sortear 5 números entre 1 e 10
    for cont in range(0, 5):
        n = randint(1, 10)
# Colocando o número sorteado na lista
        lista.append(n)
        print(f'\033[1;35m{n} \033[m', end='', flush=True)
        sleep(0.3)
    print('- PRONTO!')

# Definindo a função "somaPar"
def somaPar(lista):
    soma = 0
# Verificando se os valores são pares e, se forem, fazendo a soma deles
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos números pares da {lista} é \033[1;34m{soma}\033[m.')


# Programa Principal
# Criando a lista "números"
números = list()
sorteia(números)
somaPar(números)
