# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e área de {}m²'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede você precisará de {} litros de tinta!'.format(tinta))
