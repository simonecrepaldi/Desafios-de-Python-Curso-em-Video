# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário de elas podem ou não formar um triângulo.

print('Vamos analisar as retas!')
print(' ')
a = float(input('Digite o comprimento da reta a: '))
b = float(input('Digite o comprimento da reta b: '))
c = float(input('Digite o comprimento da reta c: '))
print(' ')
if ((b - c) < a < (b + c)) and ((a - c) < b < (a + c)) and ((a - b) < c < (a + b)):
    print('As três retas podem formar um triângulo!')
else:
    print('As três retas não formam um triângulo!')
print(' ')

# Outra maneira de escrever esse exercício
if a < b + c and b < a + c and c < a + b:
    print('As três retas podem formar um triângulo!')
else:
    print('As três retas não podem formar um triângulo!')
    