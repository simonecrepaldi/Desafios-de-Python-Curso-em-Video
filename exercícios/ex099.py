# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# Importando a biblioteca
from time import sleep
# Definindo a função "linha" e a função "maior"
def linha():
    print('-'*50)
def maior(* num):
    cont = maior = 0
    print('\033[1;35mAnalisando os valores...\033[m')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print(f'Foram informados \033[1;33m{cont}\033[m valores.')
    print(f'O maior valor informado foi o \033[1;33m{maior}\033[m.')


# Programa Principal
linha()
maior(6, 3, 8, 1, 2, 0, 7)
linha()
maior(3, 9, 1, 4, 6, 5)
linha()
maior(7, 5)
linha()
maior(6)
linha()
maior()
linha()
