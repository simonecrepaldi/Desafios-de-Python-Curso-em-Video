# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o

s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if (n%2)==0:
        s += n
        cont += 1
print('A soma do(s) {} número(s) par(es) é: {}{}{}.'.format(cont, '\033[1:33m', s, '\033[m'))
