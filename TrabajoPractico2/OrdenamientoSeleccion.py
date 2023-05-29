import numpy as np

DIM = 4
vectorA = np.empty(DIM,dtype=int)
vectorA = np.array([1,3,5,9])

i = 0
while i < DIM-1:
    p = i
    j = i + 1
    while j < DIM:
        # En este condicional el signo "< o >" determina el orden ascendente o descendente
        if vectorA[j] > vectorA[p]:
            p = j
        j += 1
    aux = vectorA[p]
    vectorA[p] = vectorA[i]
    vectorA[i] = aux
    i += 1

print(vectorA)