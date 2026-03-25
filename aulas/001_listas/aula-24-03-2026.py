# Criando uma lista e fazendo sua exibição
comidas = ['pizza','churrasco','sorvete','bacon','hotdog','alface']
print(comidas)

len(comidas)        # conta o tamanho da lista
print(len(comidas)) # imprime resultado do comando que conta o tamanho da lista

tamanho_da_lista=len(comidas)   # jogou o tamanho para uma variável
print(tamanho_da_lista)         # imprimindo a variável com o tamanho

texto="obabaotudobao"
print(f"O tamanho de {texto} é {len(texto)} ")

print(comidas[0])   # imprime o primeiro elemento da lista
print(comidas[2])   # imprimindo o 3º elemento da lista

print(f'O último elemento é "{comidas[-1]}"')
print(f"O último elemento é '{comidas[-1]}'")

# gerando uma lista
range(10) # cria um objeto referente a esta "faixa" de dados
list(range(10)) # gera a lista com base na "faixa" definida
print(list(range(10))) # imprime o range como uma lista

print(list(range(2,10))) #gerou lista de "2" até valor antes do "10"
print(list(range(20,30))) #gerou lista de 20 a 29
print(list(range(20,30,2))) # gerou a mesma lista, porém contando de 2 em 2

print(f'Comidas = {comidas}')
comidas.reverse()  # inverte a lista
print(f'Comidas = {comidas}')

# ADICIONANDO ELEMENTOS NA LISTA
comidas.append('lasanha')     # adiciona item ao final da lista
print(f'Comidas = {comidas}')

comidas.insert(0,'feijoada') # adiciona na primeira posição da lista
print(f'Comidas = {comidas}')



'''
Voc� foi contratado para organizar a playlist de um show. O sistema inicial j� possui algumas m�sicas cadastradas, mas voc� poder� interagir com ele.

Crie um programa em Python que:
    1. Crie uma lista chamada playlist com as seguintes m�sicas:
['rock', 'pop', 'jazz', 'blues', 'rap']
    2. Mostre:
        ? A lista completa
        ? O tamanho da lista
    3. Pe�a ao usu�rio:
        ? Uma nova m�sica para adicionar ao FINAL da playlist
        ? Uma m�sica para adicionar no IN�CIO da playlist
    4. Mostre novamente a playlist atualizada
    5. Inverta a ordem da playlist e mostre o resultado
'''

# 1. Criando a playlist
playlist = ['rock', 'pop', 'jazz', 'blues', 'rap']

# 2. Exibindo lista e tamanho
print(f'Playlist = {playlist}')
print(f'Tamanho da playlist = {len(playlist)}')

# 3. Inputs do usuário
nova_musica_final = input('Digite uma música para adicionar ao FINAL: ')
playlist.append(nova_musica_final)
nova_musica_inicio = input('Digite uma música para adicionar no INÍCIO: ')
playlist.insert(0, nova_musica_inicio)

# 4. Mostrando lista atualizada
print(f'Playlist atualizada = {playlist}')

# 5. Invertendo a playlist
playlist.reverse()
print(f'Playlist invertida = {playlist}')
