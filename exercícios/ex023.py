# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# Ex: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

numero = int(input('Digite um número inteiro entre 0 e 9999: '))
print('Analisando o número {}'.format(numero))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

# Obs: Se fizer da forma abaixo, se o número tiver menos de 4 dígitos (ex: 925) vai dar erro.
# print('Unidade: {}'.format(numero[3]))
# print('Dezena: {}'.format(numero[2]))
# print('Centena: {}'.format(numero[1]))
# print('Milhar: {}'.format(numero[0]))
