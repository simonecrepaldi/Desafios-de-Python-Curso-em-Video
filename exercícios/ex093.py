# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# Criando o dicionário "jogador" e a lista "totgols"
jogador = dict()
totgols = list()

jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Partidas jogadas do {jogador["nome"]}: '))

# O usuário deve informar quantos gols o jogador fez em cada partida e adicionar os valores na lista "totgols"
for c in range(1, partidas+1):
    totgols.append(int(input(f'Gols feitos na partida {c}: ')))
# Fazendo uma cópia da lista "totgols" para o dicionário "jogador" para a chave "gols" e a soma de gols para a chave "total"
jogador['gols'] = totgols[:]
jogador['total'] = sum(totgols)

# Mostrando o dicionário "jogador"
print('.'*50)
print(jogador)
print('.'*50)

# Mostrando as chaves (k) e os respectivos valores (v) do dicionário "jogador"
for k, v in jogador.items():
    print(f'    - O campo {k} tem o valor {v}')
print('.'*50)

# len(jogador["gols"]) mostra o comprimento da lista "totgols", ou seja, número de partidas jogadas (poderia substituir por {partidas})
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

# Mostrando os gols feitos em cada partida
for i, v in enumerate(jogador['gols']):
    print(f'   - Na partida {i+1} fez {v} gols.')
# Mostrando a soma de gols que o jogador fez
print(f'Foi um total de {jogador["total"]} gols.')
