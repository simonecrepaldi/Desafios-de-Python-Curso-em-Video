# Adicione ao módulo moeda.py criado nos desafios anteiores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

# Importando "moeda" de "ex110"
from ex110 import moeda

p = float(input('Digite o preço: R$'))
# Se não escrever nada aqui ele assume os valores definidos na função resumo
moeda.resumo(p, 30, 50)
