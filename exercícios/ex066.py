# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = soma = contagem = 0

# Enquanto o usuário não digitar "999", o programa continua pedindo para digitar um valor
while True:
    numero = int(input('Digite um valor (999 para parar): '))

# Quando digitar "999", programa encerra
    if numero == 999:
        break
    soma += numero
    contagem += 1
print(f'\033[1:32mA soma dos {contagem} valores digitados é {soma}!\033[m')
