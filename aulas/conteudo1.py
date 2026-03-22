# LISTAS: noções básicas
# Lista é um tipo de estrutura em que os dados são organizados de forma linear. 
# Estes podem ser acessados através de um índice que começa na posição "0" (zero).

# 1 criando uma lista
print("---|1|---")
lista = ['pizza','churrasco','sorvete','bacon']
print(lista)

# 2 Obtendo o TAMANHO da lista, isto é, quantas posições existem na coleção de dad
print("---|2|---")
len(lista)

# 3 Exibindo o conteúdo de uma posição específica da lista:
print("---|3|---")
print(lista[0])

# 4 Como eu faço para imprimir o conteúdo da última posição da lista, sem saber o tamanho da mesma?
print("---|4|---")
print(lista[len(lista)-1])
print(lista[-1])   # índice negativo, sendo -1 o último item.

# 5 Criando uma lista de números pares de -10 a 10 usando a função "range". 
# Neste caso, o comando "list" é utilizado para demonstrar o resultado obtido. 
# (veja que isto não equivale ao comando print, ou seja, o usuário final não vai ver esta saída)
print("---|5|---")
list(range(-10,11,2))

# 6 Para que o resultado acima seja realmente impresso para o usuário, basta incluir um "print":
print("---|6|---")
print(list(range(-10,11,2)))

# 7 Invertendo o conteúdo de uma lista:
print("---|7|---")
lista.reverse()
print(lista)

# 8 Criando uma nova variável x que recebe os números pares entre 0 e 21:
print("---|8|---")
x = list(range(0,21,2))
print(x)

# 9 É possível transformar uma sequência de caracteres em uma lista:
print("---|9|---")
y=list('hello world')
print(y)

# 10 Também é possível apenas imprimir uma lista de maneira invertida, sem alterar seu conteúdo.
# importante: isso não é uma ordenação, apenas inverte a ordem
print("---|10|---")
print(y[::-1])
print(y)

# 11 É possível criar uma nova lista, inicializando-a sem nenhum conteúdo:
print("---|11|---")
A = []

# 12 ADICIONAR valores de forma incremental, isto é, ao final da lista:
print("---|12|---")
A.append(12)
print(A)
A.append(19)
print(A)

# 13 E para adicionar conteúdos no início da lista (posição "0"), pode-se fazer:
print("---|13|---")
A.insert(0,33)
print(A)

# 14 Outra maneira de fazer a inserção ao início ou final da lista pode ser:
print("---|14|---")
L = [1,2,3,4]
print(L)

# adicionando ao final da lista
L = L + [40]
print(L)

# adicionando ao início da lista
L = [22] + L
print(L)

# 15 Inserindo conteúdo no meio da lista:
print("---|15|---")
print('Lista com total de posições = \'par\': ',end='')
lista = [101,102,103,104]
print(lista)

# calculando o meio da lista e transformando o resultado em "integer"
meioDaLista = int(len(lista)/2)

lista.insert(meioDaLista,'aqui é o meio' )
print(lista)

print(f'Lista com total de posições = "ímpar": {lista}')
lista2 = [101,102,103,104,105]
print(lista2)

# 16 # Inserindo mais de um elemento simultaneamente:
print("---|16|---")
listaX = [1,2,3,4,5]
print(listaX)

listaX += [10,11,12]
print(listaX)

listaX = [20,21,22] + listaX
print(listaX)

# inserindo um dado tipo "lista" no MEIO da lista
listaX.insert( int(len(listaX)/2),['a','b','c'])
print(listaX)

# inserindo um dado tipo "lista" no FINAL da lista
listaX.append([111,222,333])
print(listaX)

# imprimindo o conteúdo da última posição da lista, que é um dado do tipo "lista"
print(listaX[len(listaX)-1])

# 17 Para REMOVER itens da lista, sugere-se fazer das seguintes formas:
print("---|17|---")
lista=['aa','bb','cc','dd']
print(f'Conteúdo da lista: {lista}')

# removendo elemento informando a "posição" do mesmo.
del lista[2]
print(f'Conteúdo da lista após remover o elemento 2: {lista}')

# removendo elemento e ao mesmo tempo obtendo o elemento retirado (informando a "posição" do mesmo)
lista2=[lista.pop(1)]
print(f'Conteúdo da lista após remover o elemento 1: {lista}')
print(f'Conteúdo da lista2 que recebeu o elemento retirado da primeira lista: {lista2}')

# removendo da lista a primeira ocorrência informada. Se não estiver na lista, gera um erro.
X = ['aa','bb','cc','dd']
print(f'Lista completa: {X}')
tirar=input('Digite qual elemento você quer remover: ')
X.remove(tirar)
print(f'Resultado: {X}')

# 18 COPIA de listas (inteira ou parcial) requer uma sintaxe que merece atenção:
print("---|18|---")
L1 = ['a','b','c','d','e','f']

#ERRADO - desta forma, o L2 funcionará como um "apelido" para L1. Ambos os nomes referenciam ao mesmo objeto.
L2 = L1

#CORRETO - desta forma, uma nova lista L2 receberá como conteúdo a cópia do conteúdo de L1
L2 = L1[:]

print(f'Lista completa: {L1}')
print(f'Imprimindo do início até a posição 2: {L1[:2]}')
print(f'Imprimindo após a posição 4 em diante: {L1[4:]}')
print(f'Imprimindo após a posição 1 em diante: {L1[1:]}')
print(f'Imprimindo os 2 últimos elementos: {L1[-2:]}')
print(f'Imprimindo penúltima posição (-2, contando a segunda posição de trás p/ frente): {L1[-2]}')

#copiando os 3 últimos elementos de L1 para L3
L3 = L1[-3:]
print(f'O conteúdo de L3 é {L3}')


# 19 Ordenando uma lista em ordem crescente ou decrescente
print("---|19|---")
a = [32,10,-5,1375,12]
print(f'Conteúdo original: {a}')

a.sort()
print(f'Conteúdo ordenado de forma crescente: {a}')

a.sort(reverse=True)
print(f'Conteúdo ordenado de forma decrescente: {a}')

# 21 
b = ['hello','oi','abacate']

print(f'Conteúdo original da lista: {b}')

b.sort()
print(f'Conteúdo ordenado de forma crescente: {b}')

# 20 Identificando o maior e menor em uma lista:
# Também é possível imprimir de forma ordenada, 
# mas sem alterar o posicionamento dos elementos na lista original.
print("---|20|---")
lista = ['obabao','tudobem','comovai']
print('Lista impressa de modo ordenado: \t\t{}'.format(sorted(lista)))
print('Lista impressa c/ posicionamentos originais: \t{}'.format(lista))

L = [19,15,-20,924]
print(f'A lista contém: {L}')
print(f'O maior número da lista é {max(L)}')
print(f'O menor número da lista é {min(L)}')

# 21 LIMPAR uma lista
print("---|21|---")
lista = [1,2,3]
print(lista)
lista.clear()
print(lista)
