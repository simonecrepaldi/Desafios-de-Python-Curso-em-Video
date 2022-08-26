# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

print('\033[4mEsses são os números pares que estão no intervalo entre 1 e 50\033[m:')
for x in range(2, 51, 2):
    print(x, end=' ')
    