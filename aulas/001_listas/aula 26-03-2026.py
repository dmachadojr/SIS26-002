# aula 26-03-2026

# ESTRUTURAS DE REPETIÇÃO

'''
for i in '1','2',8,2+2,'abobrinha',True,'subi no ônibus',len('obabão'):
    print(i)

for i in [1,2,3,4]:
    print(i)

A = ['agrião','rúcula','berinjela','abobrinha','couve-flor',3,19,2457]
for x in A:
    print(x)

for y in range(0,6):
    print(y)


#x = 0
#while x < 10:  #enquanto x for menor do que 10, faça
#    x = float(input('Digite um valor para x: '))
#    print(f'Foi digitado {x}. Vou continuar rodando.')
'''

'''
senha = 'secreto'
m = ''
while m != senha:
    m=input('Digite a senha: ')
'''


#senha2 = 'secreto2'
#while input('Digite a senha: ') != senha2:
#    print('Senha incorreta.')

'''
nota=float(input('Digite uma nota (0-100): '))
while nota < 0 or nota > 100:
    nota=float(input('Nota inválida. Tente novamente: '))
print(f'A nota válida digitada foi {nota}')


while True:
    n=int(input('Digite um número inteiro: '))
    print(f'Você digitou {n}')
    if n == 9:
        print('Parabéns, agora podemos sair do loop')
        break
'''

# Crie um código que:
#  - receba 5 itens, 
#  - faça a ordenação da lista
#  - exiba a lista ordenada
#  - crie uma segunda lista que contenha a lista1 invertida.

'''
meus_itens = []                            # lista precisa ser declarada inicialmente para uso.

for i in range(1,6):                    # faz a contagem de 1 a 5
    item = input(f'Digite o item {i}: ')  # input de item
    meus_itens.append(item)              # adiciona item ao final da lista

meus_itens.sort()                        # faz a ordenação definitiva da lista
print(meus_itens)                        # exibe a lista em ordem alfabética

# criando uma segunda lista com os itens organizados na ordem alfabética invertida
meus_itens_invertido=sorted(meus_itens, reverse=True)
print(meus_itens_invertido)

# exibindo a lista ordenada e de uma maneira mais "humana"
print()
print("Exibição da lista em ordem alfabética")
for x in range(len(meus_itens)):
    print(f"item {x+1}: {meus_itens[x]} ")
'''

# RECURSIVIDADE: 
comidas = ['bacon','lasanha','churrasco']
frutas = ['pera','uva','jabuticaba']

for x in comidas:
    print(x)

for y in frutas:
    print(y)

contador = 0
for x in comidas:
    for y in frutas:
        print(x,y)
        contador+=1   #incrementa contador
print(f'Foram identificados \033[1m{contador}\033[0m combinações.')


