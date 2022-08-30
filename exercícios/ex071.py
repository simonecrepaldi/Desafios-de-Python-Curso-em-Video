# Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cont = 0
print('='*40)
print('\033[1;34mCAIXA ELETRÔNICO\033[m'.center(47))
print('='*40)

valor = int(input('Quanto você deseja sacar? R$'))
total = valor

# Definindo cédula como o maior valor disponível (R$50)
cédula = 50
totalced = 0

# Verificando a quantidade de cédulas de R$50, até que o total a ser sacado seja < que R$50
while True:
    if total >= cédula:
            total -= cédula
            totalced += 1

# Se tem pelo menos uma cédula de R$50, totalced é a quantidade de cédulas de R$50
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${cédula}')

# Para total < 50, a cédula passa a ser de R$20
        if cédula == 50:
            cédula = 20

# Para total < 20, a cédula passa a ser de R$10
        elif cédula == 20:
            cédula = 10

# Para total < 10, a cédula passa a ser de R$1
        elif cédula == 10:
            cédula = 1
    
# Como R$1 é o menor valor, o programa para quando total = 0
        totalced = 0
        if total == 0:
            break

print('='*40)
print('\033[1;31mTRANSAÇÃO ENCERRADA!\033[m'.center(50))
print('='*40)
