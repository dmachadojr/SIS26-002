vetorPossibilidade = [True,False]
print("--------------------------------")
print("Fórmula: (M v N) ^ ¬(O v P) ^ (¬M v Q) ^ (¬N v R)")
print("--------------------------------")
linhas = 0

for M in vetorPossibilidade:
    for N in vetorPossibilidade:    
        for O in vetorPossibilidade:
            for P in vetorPossibilidade:
                for Q in vetorPossibilidade:
                    for R in vetorPossibilidade:
                        if (M or N) and not (O or P) and (not M or Q) and (not N or R):
                            resultadoFormula='Verdadeiro'
                        else:
                            resultadoFormula='Falso'
                        print(f'M = {M} \t N = {N} \t O = {O} \t P = {P} \t Q = {Q} \t R = {R} \t FÓRMULA={resultadoFormula}')
                        linhas += 1
print(f'Total de linhas: {linhas}')
