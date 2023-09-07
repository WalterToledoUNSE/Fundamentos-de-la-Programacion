# Cargar los datos en el vector. Ordenarlo en forma ascendente un vector A
# de 10 elementos, y luego mostrarlo ordenado.

import numpy as np

# Definición de Módulos
def cargarVector(A, dimA):
    A = [2,5,6,9,8,6,10,88]
    dimA = 8
    return A, dimA

def ordenarVector(A, dimA):
    i = 0
    while i < dimA - 1:
        p = i
        j = i + 1
        while j < dimA:
            # En este condicional el signo "< o >" determina el orden ascendente o descendente
            if A[j] < A[p]:
                p = j
            j += 1
        aux = A[p]
        A[p] = A[i]
        A[i] = aux
        i += 1
    return A

def mostrarVector(A,dimA):
    for i in range(dimA):
        print(A[i],end=" ")

    return None

# Programa Principal
DIM = 10
dimA = 0

vectorA = np.empty(DIM,dtype=int)
vectorA, dimA = cargarVector(vectorA, dimA)
print("El vector ingresado es el siguiente:")
mostrarVector(vectorA, dimA)
vectorA = ordenarVector(vectorA, dimA)
print("\nEl vector ordenado es el siguiente:")
mostrarVector(vectorA, dimA)

