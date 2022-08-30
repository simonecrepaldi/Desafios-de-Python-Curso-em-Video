# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

# Criando o dicionário "jogador" e as listas "partidas" e "time"
jogador = dict()
partidas = list()
time = list()

while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).title()
    tot = int(input(f'Partidas jogadas do {jogador["nome"]}: '))
# Para limpar os gols do jogador anterior, quando for ler o do jogador atual
    partidas.clear()
    for c in range(1, tot+1):
        partidas.append(int(input(f'Gols feitos na partida {c}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
# O programa só vai aceitar "S" ou "N" e se escolher "N" ele encerra
    while True:
        resp = str(input('\033[1;33mQuer continuar? [S/N] \033[m')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda S ou N!')
    if resp == 'N':
        break
print('-'*45)
print('cod ', end='')
# Para mostrar o cabeçalho no resumo
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*50)
# Aqui vai mostrar o nome, gols e total de gols dos jogadores
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*50)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    print('')
# Para parar e não mostrar dados de mais nenhum outro jogador
    if busca == 999:
        break
# Não tem como mostrar dado de jogador com código maior que o comprimento de "time"
    if busca >= len(time):
        print(f'\033[1;31mERRO! Não existe jogador com o código {busca}!\033[m')
    else:
        print(f'\033[1;35mLEVANTAMENTO DE DADOS DO JOGADOR {time[busca]["nome"]}:\033[m')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    >> No jogo {i+1} fez {g} gols.')
        print('')
print('.'*50)
