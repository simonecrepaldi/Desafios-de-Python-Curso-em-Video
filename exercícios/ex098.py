# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

# Importando a biblitoeca
from time import sleep
# Definindo a função "contador"
def contador(i, f, p):
# Para quando escolher um p negativo, tem que transformar ele em +
    if p < 0:   
        p *= -1
# Como o passo não pode ser 0, fazemos p = 1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'\033[1;36mContagem de {i} até {f}, de {p} em {p}:\033[m')
    sleep(1)
# Caso a contagem for aumentando (+ passo)
    if i < f:
        cont = i
# Vai começar de i e depois vai fazer (i + p) até isso ser = f
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
# Para quando a contagem for diminuindo (- passo)
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
# Como é pra tirar o p, então usa "-="
            cont -= p
        print('FIM!')
    print('-=' * 20)
    print(' ')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('\033[1;35mAgora é a sua vez de personalizar a contagem!\033[m')
i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
contador(i, f, p)
