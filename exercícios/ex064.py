#Crie um programa que leia vários números inteiros pelo teclado. O programa vai parar quando o usuário digitar o valor 999 (flag), que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cores = {'limpa':'\033[m',
         'amarelo':'\033[1;33m'}

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('{}Você digitou {} números e a soma deles é {}.{}'.format(cores['amarelo'], cont, soma, cores['limpa']))
