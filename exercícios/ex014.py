# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite a temperatura em ºC: '))
f = (c * 1.8) + 32
k = c + 273.15
print('A temperatura de {}°C equivale a {}°F e {}K.'.format(c, f, k))

# Obs1: Para transformar de °F para °C: (f - 32) / 1.8
# Obs2: Para transformar de °C para TK: c + 273.15
