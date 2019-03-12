conjuntoUniverso = [1,2,3,4,5]
conjuntoA = [4,5,6,7,8]
complemento = []
for elementoUniverso in conjuntoUniverso:
    if elementoUniverso not in conjuntoA:
        complemento.append(elementoUniverso)
print('~A: ',complemento)
