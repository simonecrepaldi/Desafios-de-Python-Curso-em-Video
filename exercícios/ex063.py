# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

cores = {'limpa':'\033[m',
         'roxo':'\033[35m',
         'amarelo':'\033[1;33m'}

print('* '*30)
print('{}SEQUÊNCIA DE FIBONACCI{}'.center(62).format(cores['roxo'], cores['limpa']))
print('* '*30)

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1

print('* '*30)
print('{}Os {} primeiros elementos da sequência de Fibonacci são: {}'.format(cores['roxo'], n, cores['limpa']))
print('{} → {} '.format(t1, t2), end='')

cont = 3
while cont <= n:
    t3 = t1 + t2
    print('→ {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('→ {}FIM!{}'.format(cores['amarelo'], cores['limpa']))
