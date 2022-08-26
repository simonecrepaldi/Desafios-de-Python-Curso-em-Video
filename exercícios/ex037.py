# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversâo:
# (1) para binário
# (2) para octal
# (3) para hexadecimal

num = int(input('Digite um número inteiro: '))
print('')
print('''\033[4mBases de conversão\033[m:
(1) converter para BINÁRIO
(2) converter para OCTAL
(3) converter para HEXADECIMAL''')
print('')
x = int(input('Escolha a base de conversão: '))
print('')
if x == 1:
    print ('{} convertido para BINÁRIO é igual a {}.'.format(num, bin(num)[2:]))
elif x == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num)[2:]))
elif x == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente!')

# Obs1: Estamos colocando [2:] na frente do |bin, oct e hex| para "fatiar" a string, dessa forma vai mostrar a partir da 3a posição [2:]
# Obs2: Se não usar o [2:] vai aparecer na frente de cada resultado 0b (binário), 0o (octal) e 0x (hexadecimal)
