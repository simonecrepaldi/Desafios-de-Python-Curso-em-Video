# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

#Importando a biblioteca math
import math

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.sqrt(co * co + ca * ca)

print('O comprimento da hipotenusa do triângulo retângulo é: {:.2f}'.format(hip))

# Obs1: Na biblioteca math tem uma função de hipotenusa chamada hypot: hip = math.hypot(co, ca)

# Obs2: Uma outra forma de fazer sem importar a biblioteca math:
# hip = (co*co + ca*ca) ** (1/2) ou hip = (co**2 + ca**2) ** (1/2)
