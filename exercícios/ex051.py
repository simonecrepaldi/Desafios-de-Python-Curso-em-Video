# Desenvolva um programa que leia o primeiro termo e a razão de uma PA
# No final, mostre os 10 primeiros termos dessa progressão

print('* '*20)
print('Analisando os 10 termos da PA'.center(40))
print('* '*20)

a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
print('* '*20)

print('\033[1;33mOs 10 primeiros termos da PA são\033[m: ')
if r != 0:
     for c in range(a, (10*r)+a, r):
          print(c, end=' → ')
else:
     for c in range(a, 10+a):
          print(a, end=' → ')
print('FIM!')
