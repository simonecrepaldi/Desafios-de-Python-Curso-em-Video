# Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

# Importando as bibliotecas
from random import randint
from time import sleep

# Fazendo o computador escolher um número entre 0 e 10
comp = randint(0, 10)

cont = 1
print('-=-'*20)
print('Pensei em um número inteiro entre 0 e 10!')
print('-=-'*20)

# Tentando adivinhar qual foi o número entre 0 e 10
num = int(input('Em que número eu pensei? '))

print('\033[1;35mPROCESSANDO.....\033[m')
sleep(1)
while num != comp:
    if num > comp:
        print('Hum... menos! Tente novamente!')
    else:
        print('Hum... mais! Tente novamente!')
    num = int(input('>>> Chute outro número: '))
    cont += 1
print('\033[36mPARABÉNS! Você acertou em {} tentativa(s)!\033[m'.format(cont))


# Outra forma de resolver:
from random import randint
computador = randint(0, 10)
print('Adivinhe em qual número entre 0 e 10 eu pensei!')
acertou = False
tentativa = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    tentativa += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente de novo!')
        elif jogador > computador:
            print('Menos... Tente de novo!')
print('Você acertou com {} tentativas!'.format(tentativa))
