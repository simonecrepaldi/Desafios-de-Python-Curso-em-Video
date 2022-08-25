# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# Importando a bilbioteca math
from math import radians, sin, cos, tan

ang = float(input('Digite um ângulo qualquer: '))

# Convertendo o ângulo de graus para radianos
rad = radians(ang)

sen = sin(rad)
cos = cos(rad)
tan = tan(rad)

print('O valor do seno, cosseno e tangente de {:.2f}º é {:.4f}, {:.4f} e {:.4f}, respectivamente.'.format(ang, sen, cos, tan))

# Obs: Outra maneira de resolver o exercício, sem converter primeiro o ângulo para radianos:
# seno =  sin(radians(ang))
# cosseno = cos(radians(ang))
# tangente = tan(radians(ang))
