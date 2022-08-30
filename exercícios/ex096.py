# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

# Definindo a função "área"
def área(l, c):
    a = c * l
    print(f'>>> Um terreno com {l:.2f}m de largura e {c:.2f}m de comprimento tem uma \033[1;35márea igual a {a:.2f}m²\033[m.')


# Programa Principal
l = float(input('Largura do terreno em metros: '))
c = float(input('Comprimento do terreno em metros: '))
área(l, c)
