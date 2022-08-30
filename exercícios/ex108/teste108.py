# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

# Importando "moeda" de "ex108"
from ex108 import moeda

p = float(input('Digite o preço: R$'))
taxa = int(input('Digite o valor da taxa (em %): '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Diminuindo {taxa}% de {moeda.moeda(p)} temos {moeda.moeda(moeda.diminuir(p, taxa))}')
print(f'Aumentando {taxa}% de {moeda.moeda(p)} temos {moeda.moeda(moeda.aumentar(p, taxa))}')
