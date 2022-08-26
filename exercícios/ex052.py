# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

print('* '*20)
print('ANALISANDO NÚMEROS PRIMOS!'.center(40))
print('* '*20)
print(' ')

tot = 0
num = int(input('Digite um número inteiro: '))
print(f'Verificando por quais números o {num} é divisível: ', end='')
if num != 0:
    for x in range(1, num+1):
        if num % x == 0:
            print('\033[33m', end=' ')
            tot += 1
        else:
            print('\033[35m', end=' ')
        print('{}'.format(x), end=' ')
    print('')
    print('\n\033[mO número {} é divisível por {} números.'.format(x, tot))

if tot == 2:
    print('E por isso ele \033[1;32mÉ PRIMO\033[m!')
else:
    print('E por isso ele \033[1;31mNÃO É PRIMO\033[m!')

# Os números em amarelo mostram quantas vezes o 'num' foi divisível. 
# Número primo é só divisível por ele mesmo e por 1.
