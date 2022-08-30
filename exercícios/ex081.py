#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# a) Quantos números foram digitados.
# b) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.

# Criando a lista em branco
lista = []
cont = 0

while True:
    num = int(input('Digite um valor: '))
    resposta = str(input('Deseja continuar? [S/N] ')).upper()
    cont += 1
    lista.append(num)

# Se a resposta não for "S" encerra o programa
    if resposta not in 'S':
        break

# Colocando os números em ordem decrescente (reverse=True)
lista.sort(reverse=True)

print('-'*55)
#Se quiser pode usar {len(lista)} para saber a quantidade de elementos da lista
print(f'\033[1;34ma) Total de valores digitados: {cont}.\033[m')
print(f'\033[1;35mb) Valores em ordem decresente: {lista}\033[m')

# Analissando se o "5" faz parte da lista e mostrando uma das duas mensagens
if 5 in lista:
    print('\033[1;33mc) O valor 5 faz parte da lista.\033[m')
else:
    print('\033[1;33mc) O valor 5 não faz parte da lista.\033[m')
print('-'*55)
