# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o seu salário? R$'))
if salario>1250:
    print('O valor do seu salário com um aumento de 10% será de R${:.2f}!'.format(salario*1.1))
else:
    print('O valor do seu salário com um aumento de 15% será de R${:.2f}!'.format(salario*1.15))
