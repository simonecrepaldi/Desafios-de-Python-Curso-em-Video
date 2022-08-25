# Crie um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR

num = int(input('Digite um número inteiro qualquer: '))
x = num%2
if x==0:
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é ÍMPAR!'.format(num))

# Obs: O resto da divisão (%) de qualquer número para é 0 e de qualquer número ímpar é 1!