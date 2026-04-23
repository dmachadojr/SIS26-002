possibilidade = [True,False]
print("--------------------------------")
print("Fórmula: (P v Q) ^ ¬R")
print("--------------------------------")

for P in possibilidade:
    for Q in possibilidade:
        for R in possibilidade:
            if (P or Q) and not R:
                res_f = 'Verdadeiro'
            else:
                res_f = 'Falso'
            print(f'P = {P} \tQ = {Q} \tR = {R} \tFórmula = {res_f}')
