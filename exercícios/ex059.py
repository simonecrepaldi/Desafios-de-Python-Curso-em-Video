# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar | [2] multiplicar | [3] maior | [4] novos números | [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m'}

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

opção = 0

while opção != 5:
    print('''OPÇÕES DISPONÍVEIS: 
    [1] somar os valores
    [2] multiplicar os valores
    [3] descobrir qual dos valores é o maior
    [4] escolher novos números
    [5] sair do programa''')
    opção = int(input('Qual a sua escolha? '))
    if opção == 1:
        print('{}A soma entre {} e {} é {}.{}'.format(cores['amarelo'], n1, n2, n1+n2, cores['limpa']))
    elif opção ==2:
        print('{}O valor de {} x {} é {}.{}'.format(cores['amarelo'], n1, n2, n1*n2, cores['limpa']))
    elif opção == 3:
        if n1 > n2:
            print('{}O maior valor digitado é: {}.{}'.format(cores['amarelo'], n1, cores['limpa']))
        else:
            print('{}O maior valor digitado é: {}.{}'.format(cores['amarelo'], n2, cores['limpa']))
    elif opção == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
print('')
print('* ' * 20)
print('{}Programa finalizado!{}'.format(cores['vermelho'], cores['limpa']).center(45))
print('* ' * 20)
