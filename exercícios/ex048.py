# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500

from itertools import count


print('Números ímpares e múltiplos de 3, no intervalo entre 1 e 500!')
print('')
s = cont = 0

for c in range(1, 501, 2):
       if c % 3 == 0:
              s += c
              cont += 1
print('A soma entre todos os {} números é: {}!'.format(cont, s))

# CONT - para contar a quantidade de número ímpares e múltiplos de 3 entre 1 e 500
# se colocar o CONT alinhado com o IF, ele vai contar todos os números entre 1 e 500, pulando de dois em dois (250)
