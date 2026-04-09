print("COMBINAÇÕES POSSÍVEIS")
camisas = ['Social', 'Verde', 'Regata']
calcas = ['Jeans', 'Azul', 'Bermuda']
calcados = ['Tênis', 'Sapato']

for c in camisas:
    for l in calcas:
        for s in calcados:
            if (not (c == 'Verde' and l == 'Azul')) and (s == 'Tênis' or c != 'Social'):
                print(f"Sugestão: {c}, {l} e {s}")
