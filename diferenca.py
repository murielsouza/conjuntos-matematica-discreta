conjuntoA = [1,2,3,4,5]
conjuntoB = [4,5,6,7,8]
conjuntoDiferencaAB = []
conjuntoDiferencaBA = []

for elementoDeA in conjuntoA:
    if elementoDeA not in conjuntoB:
        conjuntoDiferencaAB.append(elementoDeA)
for elementoDeB in conjuntoB:
    if elementoDeB not in conjuntoA:
        conjuntoDiferencaBA.append(elementoDeB)

print('A - B: ', conjuntoDiferencaAB)
print('B - A: ', conjuntoDiferencaBA)
