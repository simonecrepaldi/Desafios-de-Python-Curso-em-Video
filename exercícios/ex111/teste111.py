# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

# Importando "moeda" de "ex111.utilidadescev"
from ex111.utilidadescev import moeda

p = float(input('Digite o preço: R$'))
# Se não escrever nada aqui ele assume os valores definidos na função "resumo"
moeda.resumo(p, 35, 22)
