# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior valor da segunda linha.

# Criando a lista "matriz" formada por outras 3 listas
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Criando as listas "pares" e "ímpares"
pares = []
ímpares = []

somapar = maior = somacol= 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
print('-'*45)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-'*45)
print(f'a) A soma dos valores pares é: {somapar}')

for l in range(0, 3):
    somacol += matriz[l][2]
    print(f'b) A soma dos valores da terceira coluna é: {somacol}')

for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'c) O  maior valor da segunda linha é: {maior}')
