# Crie um programa que faça o computador jogar Jokenpô com você.
# pedra ganha de tesoura e perde de papel
# tesoura ganha de papel e perde de pedra
# papel ganha de pedra e perde de tesoura

# Importando as bibliotecas
from random import randint
from time import sleep

# Criando uma tupla com as três opções do jogo
itens = ('Pedra', 'Papel', 'Tesoura')

# Fazendo o computador sortear um número entre 0, 1 e 2
computador = randint(0, 2)

print('{:-^40}'.format('VAMOS JOGAR JOKENPÔ'))
print('''Suas opções são:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
print('')

# Escolha do jogador entre 0, 1 e 2
jogador = int(input('Qual é a sua jogada? '))

print('JO...', end='')
sleep(1)
print('KEN...', end='')
sleep(1)
print('PÔ!!!')
print('')
print('-*'*20)

# Mostrando o item da tupla na posição que o computador escolheu
print('Computador jogou {}!'.format(itens[computador]))

# Mostrando o item da tupla na posição que o jogador escolheu
print('Você jogou {}!'.format(itens[jogador]))

print('-*'*20)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ GANHOU!')
    elif jogador == 2:
        print('COMPUTADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador ==2:
    if jogador == 0:
        print('VOCÊ GANHOU!')
    elif jogador == 1:
        print('COMPUTADOR GANHOU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
