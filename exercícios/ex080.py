# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# Criando uma lista em branco
valores = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))

# Para o primeiro valor digitado (c == 0) e valores[-1] compara com o valor da última posição
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('O valor foi digitado no final da lista.')

    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:

# insert(pos, n) para adicionar o valor "n" na posição "pos"
                valores.insert(pos, n)
                print(f'O valor foi adicionado na posição {pos} da lista.')
                break
            pos +=1

print('*.'*35)
print(f'\033[1;35mOs valores digitados em ordem crescente foram: {valores}\033[m')
print('*.'*35)
