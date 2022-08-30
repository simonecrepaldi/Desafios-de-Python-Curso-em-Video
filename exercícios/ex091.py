# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

# Importando as bibliotecas
from random import randint
from time import sleep
from operator import itemgetter

# Criando o dicionário "jogo" com os números sorteados do dado (1 a 6)
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

# Criando a lista "ranking"
ranking = list()

print('.'*30)
print('\033[1;34mVALORES SORTEADOS!\033[m'.center(40))
print('.'*30)

# Mostrando os valores sorteados dos 4 jogadores
for k, v in jogo.items():
    print(f'- {k} tirou {v} no dado.')
    sleep(1)

print('.'*30)
print('\033[1;35mRANKING!\033[m'.center(40))
print('.'*30)

# Colocando os valores da lista "ranking" em ordem decrescente (reverse=True)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
