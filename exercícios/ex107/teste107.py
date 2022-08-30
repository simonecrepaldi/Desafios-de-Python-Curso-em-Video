# Crie um módulo chamado moeda.py que tenha funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

# Importando "moeda" de "ex107"
from ex107 import moeda

p = float(input('Digite o preço: R$'))
taxa = float(input('Digite o valor da taxa (em %): '))
print(f'A metade de R${p} é R${moeda.metade(p):.2f}')
print(f'O dobro de R${p} é R${moeda.dobro(p):.2f}')
print(f'Diminuindo {taxa:.2f}% de R${p:.2f} temos R${moeda.diminuir(p, taxa):.2f}')
print(f'Aumentando {taxa:.2f}% de R${p:.2f} temos R${moeda.aumentar(p, taxa):.2f}')
