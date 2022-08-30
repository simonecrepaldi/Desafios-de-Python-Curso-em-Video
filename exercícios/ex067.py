# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    número = int(input('Quer ver a tabuada de qual valor? '))
    print('* ' * 20)

# só considera números positivos, se for negativo encerra o programa 
    if número < 0:
        break

# range(1, 11) porque na tabuada vai de 1 a 10 (nesse caso, o 11 não conta)
    for c in range(1, 11):
        print(f'{número} x {c} = {número * c}')         
    print('* ' * 20)
print('\033[1;31mPROGRAMA TABUADA ENCERRADO!\033[m'.center(50))
