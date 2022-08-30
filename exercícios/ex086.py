# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

# Criando a lista "matriz" formada por outras 3 listas
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Usar os dois "for" para alimentar a matriz. Começa pela primeira linha (l = 0 e c = 0) e segue da esquerda para a direita, terminando em (l = 3 e c = 3)
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-'*40)

# Aqui usa o "for" pra mostrar a estrutura da matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
 # Toda vez que terminar as colunas, o "print()" quebra a linha
    print()
    