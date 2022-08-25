#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Qual é o salário do funcionário? R$'))
a = s * 1.15
print('Com um aumento de 15%, o salário do funcionário que era R${:.2f}, passa a ser R${:.2f}.'.format(s, a))
