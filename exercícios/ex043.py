# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# Acima de 40: obesidade mórbida

print('\033[1mVAMOS ANALISAR O SEU IMC?\033[m')
print('')
peso = float(input('Qual o seu peso em kg? '))
altura = float(input('Qual a sua altura em m? '))
IMC = (peso)/(altura**2)
if IMC < 18.5:
    print('O seu IMC é {:.1f}, você está \033[1mABAIXO DO PESO IDEAL\033[1m!'.format(IMC))
elif IMC >= 18.5 and IMC < 25:
    print('O seu IMC é {:.1f}, você está na faixa de \033[1mPESO IDEAL\033[m!'.format(IMC))
elif IMC >= 25 and IMC < 30:
    print('O seu IMC é {:.1f}, você está com \033[1mSOBREPESO\033[m!'.format(IMC))
elif IMC >= 30 and IMC < 40:
    print('O seu IMC é {:.1f}, você está com \033[1mOBESIDADE\033[m!'.format(IMC))
else:
    print('O seu IMC é {:.1f}, você está com \033[1mOBESIDADE MÓRBIDA\033[m!'.format(IMC))
    