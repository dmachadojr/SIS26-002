'''
RECURSIVIDADE é uma estrutura de repetição na qual existem "sub-loops", em outras palavras: um loop dentro de outro.
'''

#1 Vejamos um exemplo de recursividade usando "for":
comidas = ['bacon','lasanha','churrasco']
frutas = ['pera','uva']

for x in comidas:
    print(x)

for y in frutas:
    print(y)

print('-------| agora exibindo a combinação das duas listas, demonstrando todas as possibilidades |--------------')
for x in comidas:
    for y in frutas:
        print(x,y)


print('-------| exibindo a combinação, excluindo valores iguais|--------------')
for x in comidas:
    for y in frutas:
        if x != y:
            print(x,y)



# Mesma lógica, porém com uma lista um pouco maior:
comidas = ['bacon','lasanha','churrasco','ervilha','mingau','sopa','hamburguer','brocolis']
frutas = ['pera','uva','maça','melancia','goiaba']
contador=0

for x in comidas:
    for y in frutas:
        printf('{x} com {y}')
        contador+=1
print(f'Foram um total de {contador} combinações.')


#### EXERCÍCIO 1: Em uma cozinha de restaurante existem apenas os ingredientes a seguir. 
#Exiba todas as possíveis combinações (não importa a sequência)
#utilizando até 3 ingredientes e quantas receitas isto totaliza.
#Ingredientes disponíveis: tomate, agrião, filé de frango, pão de queijo, mel.
#obs.: não se esqueça de eliminar combinações de nomes iguais.


#### EXERCÍCIO 2: Em uma loja de departamentos haverá uma promoção imperdível na qual se o cliente comprar a combinação de 3 grupos de produtos diferentes, ele receberá um desconto de 80% no preço total da compra.
# Seu objetivo é fazer um programa que:
# - solicite ao usuário quantos produtos haverá no grupo ELETRODOMÉSTICOS (grupo1).
# - solicite a inserção do nome dos itens deste grupo.
# - solicite ao usuário quantos produtos haverá no grupo COMIDAS (grupo2).
# - solicite a inserção do nome dos itens deste grupo.
# - solicite ao usuário quantos produtos haverá no grupo UTILIDADES (grupo3).
# - solicite a inserção do nome dos itens deste grupo.
# - gere a lista de todas as combinações possíveis excluindo combinação de nomes iguais.
