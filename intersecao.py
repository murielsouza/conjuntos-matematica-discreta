conjuntoA = [1,2,3,4,5]
conjuntoB = [4,5,6,7,8]
conjuntoIntersecao = []
for elementoDeA in conjuntoA:
    if elementoDeA in conjuntoB:
        conjuntoIntersecao.append(elementoDeA)
print(conjuntoIntersecao)