# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

cores = {'limpa':'\033[m',
         'roxo':'\033[1;35m'}

cont = soma = média = maior = menor = 0
x = 'S'

# Enquanto o usuário digitar S, o programa vai continuar digitando valores
while x == 'S':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1

# O primeiro valor digitado será o maior e o menor
    if cont == 1:
        menor = maior = num

# Se já digitou 2 ou mais valores
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

# Perguntar se o usuário quer digitar mais valores, se responder "S", volta para o "while", se digitar "N" encerra o programa
    x = str(input('Gostaria de informar mais valores? [S/N]: ')).upper().strip()[0]

média = (soma) / cont
print('{}A média dos {} valores digitados é {:.2f}!'.format(cores['roxo'], cont, média))
print('O maior valor é {} e o menor é {}{}.'.format(maior, menor, cores['limpa']))
