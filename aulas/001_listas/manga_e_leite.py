frutas = []
bebidas = []

# preenchendo lista de frutas
for i in range(2):
    frutas.append(input(f"Digite a {i+1}ª fruta: "))

# preenchendo lista de bebidas
for i in range(2):
    bebidas.append(input(f"Digite a {i+1}ª bebida: "))

print("-- Kits Alimentícios identificados ---")
for f in frutas:
    for b in bebidas:
        if not (f == "manga" and b == "leite"):
            print(f"Combinação: {f} com {b}")
        else:
            print(f"Combinação: {f} + {b} **** inválida! ****")

