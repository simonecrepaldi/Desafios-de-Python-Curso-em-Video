# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais (a = b = c)
# Isósceles: dois lados iguais (a = b ou a = c ou b = c)
# Escaleno: todos os lados diferentes (a =! b =! c)

print('Vamos analisar as retas!')
a = float(input('Digite o comprimento da reta a: '))
b = float(input('Digite o comprimento da reta b: '))
c = float(input('Digite o comprimento da reta c: '))
print('')

if a < b + c and b < a + c and c < a + b:
    print('As três retas PODEM formar um TRIÂNGULO ', end='')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a != b != c != a:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('As três retas NÃO PODEM formar um TRIÂNGULO!')
