# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Apenas os 5 primeiros colocados
# b) Os últimos 4 colocados da tabela
# c) Uma lista com os times em ordem alfabética
# d) Em que posição na tabela está o time da Chapecoense

# Definindo a tupla com o nome dos 20 times
times = 'Palmeiras', 'Atlético MG', 'Corinthians', 'Internacional', \
        'Fluminense', 'Athletico PR', 'Flamengo', 'Bragantino', \
        'São Paulo', 'Ceará SC', 'Santos', 'Botafogo', 'Avaí', \
        'Goiás', 'Cuiabá', 'Coritiba', 'América MG', 'Atlético GO', \
        'Fortaleza', 'Juventude'

print('-'*50)
print('\033[1;34mTABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL\033[m'.center(60))
print('-'*50)
print(f'\033[1mLista dos Times:\033[m {times}')
print('')

# [0:5] mostra os times nas posições 0, 1, 2, 3 e 4 da tupla
print(f'a) Os cinco primeiros colocados são: {times[0:5]}')

# [16:] mostra os times que estão na posição 16 até o final (pode usar [-4:0])
print(f'b) Os quatro últimos colocados são: {times[16:]}')

# "sorted()" coloca os valores em ordem crescente
print(f'c) Times em ordem alfabética: {sorted(times)}')

# Como a Chapecoense não estava entre os 20 times, substitui pelo Internacional. "index()" mostra a posição do valor na tupla
print(f'd) O time do Internacional está na {times.index("Internacional")+1}ª posição')
