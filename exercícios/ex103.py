# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado

# Definindo a função "linha" e a função "ficha"
def linha():
    print('.'*45)
# Parâmetros para caso não seja informado algum dos dois valores
def ficha(jogador='<desconhecido>', gol=0):
    print(f'\033[1;35mO jogador {jogador} fez {gol} gol(s) no campeonato.\033[m')


# Programa Principal
nome = str(input('Nome do Jogador: ')).title()
# Deixar como string para que na hora de entrar com os valores, o usuário possa deixar em branco (caso o número de gols seja 0)
gols = str(input('Número de Gols: '))
linha()
# Se o valor informado para gols for um número inteiro, gol vai rebever esse valor
if gols.isnumeric():
    gols = int(gols)
# Caso não seja numérico ou não seja informado nada, gol recebe 0
else:
    gols = 0
# Caso não informe o nome, vai aparecer como <desconhecido>
if nome.strip() == '':
# Gol recebe o valor informado em gols
    ficha(gol=gols)
# Se digitar valor para os dois, vai retornar os dois valores digitados (nome e gols)
else:
    ficha(nome, gols)
linha()
