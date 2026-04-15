'''
Exercício 5: Cardápio de Marmitas Fitness
Enunciado: Crie três listas: proteinas, carboidratos e saladas. O sistema deve gerar as opções de montagem de marmitas para a semana, seguindo estas diretrizes:
NÃO é permitido combinar "Peixe" com "Batata Doce".
A escolha de salada "Espinafre" deve ocorrer se e somente se a proteína for "Ovo" (Biimplicação).
Não se esqueça de eliminar combinações de nomes iguais caso algum ingrediente se repita nas listas
.
Resolução Sugerida:
'''

print("OPÇÕES DE MARMITAS")
proteinas = ['Peixe', 'Ovo', 'Frango']
carboidratos = ['Batata Doce', 'Arroz', 'Quinoa']
saladas = ['Espinafre', 'Alface', 'Brócolis']

for pr in proteinas:
    for cb in carboidratos:
        for sl in saladas:
            # Regra 1: Restrição de sabor
            # Regra 2: Biimplicação (A == B)
            # Regra 3: Nomes diferentes
            if (not (pr == 'Peixe' and cb == 'Batata Doce')) and \
                ((sl == 'Espinafre') == (pr == 'Ovo')) and \
                (pr != cb and cb != sl and pr != sl):
                
                print(f"Marmita: {pr} + {cb} + {sl}")
            #else:
            #    print(f"Marmita: {pr} + {cb} + {sl} = inválido")
