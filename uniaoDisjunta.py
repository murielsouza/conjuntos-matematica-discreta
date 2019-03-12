conjuntoA = [1,2,3]
conjuntoB = [3,4,5]
uniaoDisjunta = []
for elementoDeA in conjuntoA:
    uniaoDisjunta.append([elementoDeA, 'conjuntoA'])
for elementoDeB in conjuntoB:
    uniaoDisjunta.append([elementoDeB, 'conjuntoB'])
print(uniaoDisjunta)