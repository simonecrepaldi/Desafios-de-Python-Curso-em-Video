# Faça um programa que mostre uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles

# Importando as bibliotecas
from time import sleep
import emoji

print('Contagem regressiva...')
for x in range(10, -1, -1):
    sleep(1)
    print(x)
sleep(1)
print(emoji.emojize(':fireworks: ' * 10))
