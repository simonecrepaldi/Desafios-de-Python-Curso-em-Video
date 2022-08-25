# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5.
# Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
# Importando a biblioteca que faz o computador "dormir" alguns segundos
from time import sleep 

# Fazendo o computador sortear um número entre 0 e 5
comp = randint(0, 5) 

print('-=-'*20)
print('Pensei em um número inteiro entre 0 e 5!')
print('-=-'*20)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO.....')
sleep(3)
if num==comp:
    print('PARABÉNS! Você me venceu!')
else:
    print('Ih, VOCÊ PERDEU! Eu pensei no número {} e não no {}!'.format(comp, num))
