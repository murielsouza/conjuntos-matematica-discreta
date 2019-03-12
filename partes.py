import intertools
conjuntoS = [1,2,3]
conjuntoPartes = [[]]
for i in range(len(conjuntoS) + 1):
   conjuntoPartes.append(list(itertools.combinations(conjuntoS, i)))

print(conjuntoPartes)