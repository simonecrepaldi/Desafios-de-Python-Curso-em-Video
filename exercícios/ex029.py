# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

v = float(input('Digite a velocidade atual do carro: '))
if v>80:
    print('Você foi multado por exceder o limite de velocidade de 80km/h!')
    print('O valor da multa que você terá que pagar é de R${:.2f}!'.format((v-80)*7))
print('Você está dentro do limite de velocidade, continue assim!')

# Obs: Neste caso não precisa utilizar o else. Essa estrutura é chamada de "condição simples".
