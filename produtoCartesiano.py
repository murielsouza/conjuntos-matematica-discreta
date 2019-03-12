conjuntoA = [1,2,3]
conjuntoB = [4,5]
produtoCartesianoAB = []
produtoCartesianoBA = []
for elementoDeA in conjuntoA:
    for elementoDeB in conjuntoB:
        produtoCartesianoAB.append([elementoDeA, elementoDeB])

for elementoDeB in conjuntoB:
    for elementoDeA in conjuntoA:
        produtoCartesianoBA.append([elementoDeB, elementoDeA])

print('A X B: ',produtoCartesianoAB)
print('B X A: ',produtoCartesianoBA)
