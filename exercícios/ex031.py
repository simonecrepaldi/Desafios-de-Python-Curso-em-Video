# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200km e R$0,45 para viagens mais longas.

d = float(input('Informe a distância da sua viagem em km: '))
if d<=200:
    print('A sua passagem custará R${:.2f}!'.format(d*0.50))
else:
    print('A sua passagem custará R${:.2f}!'.format(d*0.45))


#Outra forma mais simples de escrever o exercício:
d = float(input('Informe a distância da sua viagem em km: '))
if d<=200:
    preço = d*0.50
else:
    preço = d*0.40
print('O valor da sua passagem será de R${:.2f}'.format(preço))
