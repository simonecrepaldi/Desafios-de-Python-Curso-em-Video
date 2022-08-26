# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print('{:-^40}'.format(' LOJA CHICO BUTIQUE! '))
preço = float(input('Qual o valor total da compra? R$'))
print(' ')
print('''Condições de pagamento disponíveis:
[1] À vista no dinheiro ou cheque
[2] À vista no cartão
[3] No cartão em até 2x
[4] No cartão em 3x ou mais.''')
print(' ')

# Esolhendo uma opção de pagamento
pagamento = int(input('Informe qual a condição de pagamento você deseja: '))

if pagamento == 1:
    total = preço*0.9
    print('O valor total a ser pago será de R${:.2f}!'.format(total))
elif pagamento == 2:
    total = preço*.95
    print('O valor total a ser pago será de R${:.2f}!'.format(total))
elif pagamento == 3:
    total = preço
    parcela = preço/2
    print('O valor total de R${:.2f} será parcelado em 2x de R${:.2f}, sem juros!'.format(total, parcela))
elif pagamento == 4:
    total = preço*1.2
    nparc = int(input('Em quantas parcelas? '))
    parcela = total/nparc
    print('O valor total será de R${:.2f}, parcelado em {}x de R${:.2f}!'.format(total, nparc, parcela))
else:
    print('OPÇÃO INVÁLIDA! Escolha uma opção entre 1 e 4!')
print('')
print('='*40)
print('')


# Outra forma de resolver:
if pagamento == 1:
    total = preço * 0.9
elif pagamento == 2:
    total = preço * .95
elif pagamento == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}, sem juros!'.format(parcela))
elif pagamento == 4:
    total = preço * 1.2
    n = int(input('Em quantas parcelas? '))
    parcela = total / n
    print('Sua compra será parcelada em {}x de R${:.2f}!'.format(n, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA! Escolha uma opção entre 1 e 4!')
print('O total de R${:.2f} vai custar R${:.2f}!'.format(preço, total))
