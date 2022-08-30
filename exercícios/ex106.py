# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

# Importando a bibliteca
from time import sleep

# A variável 'c' é global, por isso declaramos logo no início. A lista de cores pode ser utilizada em qualquer parte do programa
c = ('\033[m',        # 0 - sem cor
     '\033[0;30:41m', # 1 - vermelho
     '\033[0;30:42m', # 2 - verde
     '\033[0;30:43m', # 3 - amarelo
     '\033[0;30:44m', # 4 - azul
     '\033[0;30:45m', # 5 - roxo
     '\033[7m',    # 6 - branco
    );

# Definindo a função principal "ajuda"
def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

# Definindo a função "título"
def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
# Se digitar "fim" o programa encerra
    if comando.upper() == 'FIM':
        break
# Mostra o manual da função ou biblioteca escolhida
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
