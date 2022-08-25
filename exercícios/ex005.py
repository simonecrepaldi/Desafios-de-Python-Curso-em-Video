#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
num1 = int(input('Digite um número: '))
num2 = num1 - 1
num3 = num1 + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}!'.format(num1, num2, num3))

#Outra forma de apresentar:
x = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}!'.format(x, (x-1), (x+1)))
