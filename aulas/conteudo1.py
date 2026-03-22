# 1 criando uma lista
lista = ['pizza','churrasco','sorvete','bacon']
print(lista)

# 2 Obtendo o TAMANHO da lista, isto é, quantas posições existem na coleção de dad
len(lista)

# 3 Exibindo o conteúdo de uma posição específica da lista:
print(lista[0])

# 4 Como eu faço para imprimir o conteúdo da última posição da lista, sem saber o tamanho da mesma?
print(lista[len(lista)-1])
print(lista[-1])   # índice negativo, sendo -1 o último item.

# 5 Criando uma lista de números pares de -10 a 10 usando a função "range". 
# Neste caso, o comando "list" é utilizado para demonstrar o resultado obtido. 
# (veja que isto não equivale ao comando print, ou seja, o usuário final não vai ver esta saída)
list(range(-10,11,2))

# 6 Para que o resultado acima seja realmente impresso para o usuário, basta incluir um "print":
print(list(range(-10,11,2)))

# 7 Invertendo o conteúdo de uma lista:
lista.reverse()
print(lista)

# 8 Criando uma nova variável x que recebe os números pares entre 0 e 21:
x = list(range(0,21,2))
print(x)

# 9 É possível transformar uma sequência de caracteres em uma lista:
y=list('hello world')
print(y)

# 10 Também é possível apenas imprimir uma lista de maneira invertida, sem alterar seu conteúdo.
# importante: isso não é uma ordenação, apenas inverte a ordem
print(y[::-1])
print(y)

# 11 É possível criar uma nova lista, inicializando-a sem nenhum conteúdo:
A = []

