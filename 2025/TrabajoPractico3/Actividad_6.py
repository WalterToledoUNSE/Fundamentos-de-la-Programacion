# Dada una matriz A(NxN) elementos. Se pide:
# 1. Generar un vector B con la sumatoria de cada fila de la matriz.
# 2. Generar un vector C con el mayor elemento de cada columna de la matriz.

import numpy as np

DIM = 5
#declaro la matriz
A = np.empty((DIM,DIM),dtype=int)
vectorB = np.empty(DIM,dtype=int)
vectorC = np.empty(DIM,dtype=int)
indiceB = 0
indiceC = 0

A = np.array([
    [41,72,27,98,53],
    [55,49,34,17,13],
    [82,67,99,85,68],
    [37,62,50,88,88],
    [51,15,76,24,96]
])

# 1. Generar un vector B con la sumatoria de cada fila de la matriz.
for i in range(DIM):
    totalFila = 0
    for j in range(DIM):
        totalFila = totalFila + A[i][j]
    vectorB[indiceB] = totalFila
    indiceB+=1

print("El vector B generado es el siguiente:")
for i in range(DIM):
    print(vectorB[i], end=" ")

# 2. Generar un vector C con el mayor elemento de cada columna de la matriz.
for j in range(DIM):
    # mayor = A[0][j] Esto es otra opción
    for i in range(DIM):
        if i == 0:
            mayor = A[i][j]
        else:
            if A[i][j] > mayor:
                mayor = A[i][j]
    vectorC[indiceC] = mayor
    indiceC += 1
print("\n")

print("El vector C generado es el siguiente:")
for i in range(DIM):
    print(vectorC[i], end=" ")

