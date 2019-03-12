conjuntoA = [1,2,3,4,5]
conjuntoB = [4,5,6,7,8]
conjuntoUniao = []
for elementoDeA in conjuntoA:
    conjuntoUniao.append(elementoDeA)
for elementoDeB in conjuntoB:
    if(elementoDeB not in conjuntoUniao):
        conjuntoUniao.append(elementoDeB)
print(conjuntoUniao)