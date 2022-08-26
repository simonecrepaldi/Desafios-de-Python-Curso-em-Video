# Faça um programa que leia o sexo de uma pessoa, mas só aceita 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

# upper() para transformar tudo em maiúsculo, strip() vai retirar espaços do início e final e [0] seleciona só a primeira letra
# Ex: Caso a pessoa digite ' masculino' vai pegar só a primeira letra 'm'

sexo = str(input('Informe o seu sexo [F/M]: ')).upper().strip()[0] 
while sexo not in 'MF':
    sexo = str(input('Dado inválido! Digite novamente seu sexo: ')).upper().strip()[0]
print('\033[34mSexo {} registrado com sucesso!\033[m'.format(sexo))

# Se quiser que o resultado apareça como 'masculino' ou 'feminino' é só incluir o código abaixo:
if sexo == 'M':
    print('Registrado: sexo masculino.')
else:
    print('Registrado: sexo feminino.')
