# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda() desenvolvida no desafio 108.

# Importando "moeda" de "ex109"
from ex109 import moeda

p = float(input('Digite o preço: R$'))
taxa = int(input('Digite o valor da taxa (em %): '))
# Usar "True" para formatar o resultado
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Diminuindo {taxa}% temos {moeda.diminuir(p, taxa, True)}')
print(f'Aumentando {taxa}% temos {moeda.aumentar(p, taxa, True)}')
