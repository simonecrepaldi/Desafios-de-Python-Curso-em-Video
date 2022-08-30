# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

pilha = []
expr = str(input('Digite a expressão: '))

# Verificando se na expressão digitada tem o símbolo "(" e se tiver adicionar na "pilha"
for símb in expr:
    if símb == '(':
        pilha.append('(')

# Se o símbolo for ")" 
    elif símb == ')':
# Se já tiver pelo menos 1 elemento na "pilha", eliminar o último elemento com "pop()"
        if len(pilha) > 0:
            pilha.pop()
# Se não tiver nenhum elemento, adicionar ")" na "pilha" e parar
        else:
            pilha.append(')')
            break

# Se o comprimento da "pilha" for 0, ou seja, se "pilha" não tiver nenhum elemento, quer dizer que os parênteses foram abertos e fechados corretamente
if len(pilha) == 0:
    print('\033[1;32mSua expressão está válida!\033[m')
# Se "pilha" tiver algum elemento, quer dizer que tem algum parênteses que naõ foi aberto e/ou fechado corretamente
else:
    print('\033[1;31mSua expressão está errada!\033[m')



# Obs: Se quiser saber apenas se a quantidade de ( ) é igual ou não, é só verificar se a quantidade de "(" é igual a ")", mas se os () estiverem na posição errada vai aparecer como se a expressão estivesse correta.
cd = ce = 0
expressão = []

expressão.append(str(input('Digite uma expressão que contenha parênteses: ')))

for exp in expressão:
    for caract in exp:
        if caract in '(':
            ce +=1
        elif caract in ')':
            cd +=1
            
    if cd == ce:
        print('\033[1:32mA expressão foi digitada é válida!\033[m')
    else:
        print('\033[1:31mA expressão digitada é inválida!\033[m')
