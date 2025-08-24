# Dado un vector V(N) se pide imprimir el índice del mayor elemento par del vector y el menor elemento impar.

import numpy as np

N = 12
V = np.empty(N,dtype=int)
V = np.array([90,31,22,29,85,24,21,5,77,33,20,30])

print("El vector original es el siguiente:")
for i in range(N):
    print(V[i], end=" ")

indiceMayor = -1
menor = 10000
mayor = 0

# Se utilizan banderas para identificar el primer elemento par mayor y el primer elemento impar menor
primerElementoPar = True
primerElementoImpar = True
for i in range(N):
    if V[i] % 2 == 0:
        # El número es par
        if primerElementoPar:
            mayor = V[i]
            indiceMayor = i
            primerElementoPar = False
        else:
            if V[i] > mayor:
                mayor = V[i]
                indiceMayor = i
    else:
        # El número es impar
        if primerElementoImpar:
            menor = V[i]
            primerElementoImpar = False
        else:
            if V[i] < menor:
                menor = V[i]

print("\n")
print("El indice del mayor elemento es el:", indiceMayor)
print("El menor elemento impar es:",menor)