# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá pergutar se o usuário vai continuar. No final, mostre:
# a) Qual é o total gasto na compra
# b) Quantos produtos custam mais de R$1000
# c) Qual é o nome do produto mais barato

menor = cont = totmil = total = 0
produto = ''
print('-'*40)
print('\033[1;35mLOJAS *X*X*X*X*\033[m'.center(50))
print('-'*40)

# strip() vai remover os espaços do início e do fim
while True:
    nome = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        produto = nome
   
# O programa só vai aceitar "S" ou "N", se digitar algo diferente vai repetir a pergunta. "N" encerra o programa
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Deseja comprar mais algo? [S/N] ')).strip().upper()[0]
    if mais == 'N':
        break

print('-'*40)
print('{:^45}'.format('\033[1;35mRESUMO DA COMPRA\033[m'))
print(f'Total gasto na compra R${total:.2f}.')
print(f'Na compra tem {totmil} produtos que custam mais de R$1000.')
print(f'O produto mais barato: {produto} por R${menor:.2f}')
