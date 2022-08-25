#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Qual é o preço do produto? R$'))
np = p * 0.95
print('O novo preço do produto com 5% de desconto é R${:.2f}!'.format(np))