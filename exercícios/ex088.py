# Faça um programa que ajude um jogador da MEGASENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# Importando as bibliotecas
from random import randint
from time import sleep

# Criando as listas "numjogo" e "jogos"
numjogo = []
jogos = []

print('.'*40)
print('\033[1;35mJOGOS DA MEGASENA\033[m'.center(50))
print('.'*40)

x = int(input('Quantos jogos você deseja fazer? '))
total = 1
print('')
print(f'\033[1;32m>>> SORTEANDO OS {x} JOGOS!\033[m')
while total <= x:
    cont = 0
    while True:
        num = randint(1, 60)

# O número só pode ser sorteado 1 vez para cada jogo, adicionar o número "num" na lista "numjogo"
        if num not in numjogo: 
            numjogo.append(num)
            cont += 1
# Como cada jogo tem 6 números, a contagem se encerra quando cont >= 6
        if cont >= 6:
            break

# Colocando os números da lista "numjogo" em ordem crescente
    numjogo.sort()

# Fazendo uma cópia da lista "numjogo" dentro de "jogos"
    jogos.append(numjogo[:])
# Depois de copiar "numjogo", apaga os valores dela para criar a próxima "numjogo" com outros 6 números
    numjogo.clear() 
    total += 1

# Fazer "{i+1}" para começar mostrando "Jogo 1", se deixar "{i}" vai aparecer "Jogo 0"
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('.' * 40)
print('BOA SORTE!'.center(40))
