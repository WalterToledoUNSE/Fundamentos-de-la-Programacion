# Determinar el mayor y el menor elemento de un vector de números enteros

import numpy as np

# Definición de Módulos
def cargarVector(A, dimA):
    A[0] = 2
    A[1] = 5
    A[2] = 6
    A[3] = 9
    A[4] = 8
    A[5] = 6
    A[6] = 1
    A[7] = 88
    dimA = 8

    return dimA

def mostrarVector(A,dimA):
    for i in range(dimA):
        print(A[i],end=" ")

    return None

def determinarMayorMenor(A,dimA):
    may = 1e-100
    men = 1e100

    for i in range(dimA):
        if(A[i]>may):
            may = A[i]
        if(A[i]<men):
            men = A[i]

    return men, may

# Programa Principal
DIM = 10
dimA = 0

vectorA = np.empty(DIM,dtype=int)

dimA = cargarVector(vectorA, dimA)
print("El vector ingresado es el siguiente:")
mostrarVector(vectorA, dimA)
menor, mayor = determinarMayorMenor(vectorA, dimA)
print("\n\nEl menor valor del vector ingresado es:",menor)
print("El mayor valor del vector ingresado es:",mayor)
