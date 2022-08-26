# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

n = int(input('Digite um número para ver sua tabuada: '))

# No for a gente determina que o 'x' vai de 1 a 10 (lembrando que o 11 não conta)
for x in range(1, 11):
    print('{} x {} = {}'.format(n, x, n*x))
