# Faça um programa que jogue par ou ímpar com o computador. O jogo será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# Importando a biblioteca
from random import randint

vitória = soma = 0

print('* '*20)
print('\033[1;35mVAMOS JOGAR PAR OU ÍMPAR!\033[m'.center(50))
print('* '*20)

while True:
# Fazendo o computador escolher um número entre 0 e 10 e pedindo para o usuário escolher um valor também
    computador = randint(0, 11)
    jogador = int(input('Diga um número: '))

# Fazendo a soma entre os dois números (computador + jogador)
    soma = jogador + computador

# Fazendo a escolha entre PAR ou ÍMPAR, se o usuário digitar algo diferente de "P" ou "I", continua pedindo para ele escolher
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar? [P/I]: ')).upper().strip()

# Mostrando o resultado e informando se a soma é PAR ou ÍMPAR
    print(f'O computador jogou {computador} e você jogou {jogador}. O total de {soma} é ', end='')
    print('PAR!' if soma % 2 == 0 else 'ÍMPAR!')

# Verificando se o jogador venceu ou perdeu
    if escolha == 'P':
        if soma % 2 == 0:
            print('\033[1;32mVOCÊ GANHOU!\033[m')
            vitória += 1
        else:
            print('\033[1;31mVOCÊ PERDEU!\033[m')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('\033[1;32mVOCÊ GANHOU!\033[m')
            vitória += 1
        else:
            print('\033[1;31mVOCÊ PERDEU!\033[m')
            break
    print('Vamos jogar novamente...')

# Quando o jogador perder, encerra o programa e mostra quantas vezes ele ganhou do computador
print(f'\033[1;35mGAME OVER!!! Você venceu {vitória} vez(es)!\033[m')
