'''
ESTRUTURAS DE REPETIÇÃO: noções básicas
Estruturas de repetição são mecanismos utilizados para que um código seja executado repetidamente até que uma condição (se disposta) seja atendida.
O "for" é um recurso em que haverá a repetição para a condição estabelecida. Por exemplo uma extensão numérica, uma sequência de caracteres, etc.
'''

#1 Fazendo um loop de repetição para exibição de uma sequência de dados:
for i in '1','2',8,2+2,'abobrinha',True,'subi no ônibus',len('obabão'):
    print(i)

#2 Fazendo um loop de repetição para exibição de uma sequência numérica:
for i in [1,2,3,4]:
    print(i)

#3 O loop também pode ser executado com base em dados já existentes em uma variável de qualquer tipo:
A = ['agrião','rúcula','berinjela','abobrinha','couve-flor',3,19,2457]
for x in A:
    print(x)

#4 A função "range" é um grande aliado de estruturas de repetições:
for y in range(0,6):
    print(y)

for i in range(0,15,2):
    print(i)

for x in range(1,11):
    print(f'Agora o i vale {x}')


#5 O "while" é um recurso em que haverá a repetição até que uma condição seja atendida.
x = 0
while x < 10:  #enquanto x for menor do que 10, faça
    x=float(input('Digite um valor para x: '))
    print(f'Foi digitado {x}. Vou continuar rodando.')

senha = '123456'
m = ''
while m != senha:
    m=input('Digite a senha: ')

nota=float(input('Digite uma nota (0-100): '))
while nota < 0 or nota > 100:
    nota=float(input('Nota inválida. Tente novamente: '))
print(f'A nota válida digitada foi {nota}')
    
#6 Também é possível forçar a "quebra" de um loop. Utiliza-se o comando "break":
while True:
    n=int(input('Digite um número inteiro: '))
    print(f'Você digitou {n}')
    if n == 9:
        print('Parabéns, agora podemos sair do loop')
        break


#7 Neste exemplo, podemos forçar o usuário a definir a quantidade de repetições:
# exemplo usando FOR
a = []
quantidade = int(input('Quantos valores serão informados? '))
for i in range(1,quantidade+1):
    a.append(input('Valor {i}: '))
print(a)

# exemplo usando WHILE
a = []
indice = 1
while indice != 99:
    valor = int(input(f'Digite o {indice}° valor (ou 99 p/ finalizar): '))
    if valor == 99:
        print('A lista possui {len(a)} valores os quais são: {a}')
        break
    a.append(valor)
    print(a)
    indice += 1

