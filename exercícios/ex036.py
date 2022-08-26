# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# Incluindo cores no programa
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m'}

valorcasa = float(input('Qual o valor da casa que você pretende comprar? R$'))
salário = float(input('Qual o seu salário atual? R$'))
anos = int(input('Em quantos anos você deseja pagar o empréstimo? '))

prestação = (valorcasa)/(anos*12)
parcelas = anos*12

if prestação < (salário*0.3):
    print('O seu empréstimo foi {}APROVADO{}!'.format(cores['verde'], cores['limpa']))
    print('O valor total de R${:.2f} deverá pago em {} parcelas de R${:.2f} cada!'.format(valorcasa, parcelas, prestação))
else:
    print('O seu empréstimo foi {}NEGADO{}!'.format(cores['vermelho'], cores['limpa']))
    print('O valor da parcela é de R${:.2f} e é maior do que R${:.2f}, que é 30% do seu salário!'.format(prestação, (salário*0.3)))
