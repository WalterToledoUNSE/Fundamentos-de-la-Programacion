import numpy as np

# Definición de Módulos
def cargarVector(A):
    A[0] = 6
    A[1] = 14
    A[2] = 5
    A[3] = 99
    A[4] = 47
    A[5] = 1
    dimA = 6

    return dimA

def mostrarVector(A,dimA):
    for i in range(dimA):
        print(A[i],end=" ")

    return None

def insertarVector(A, dimA, nro):
    b = 0
    k = 0
    while k < dimA and b == 0:
        # El condición va en función del orden de los elementos
        if nro < A[k]:
            j = dimA - 1
            while j >= k:
                A[j + 1] = A[j]
                j = j - 1
            A[k] = nro
            dimA += 1
            b = 1
        else:
            k += 1
    if b == 0:
        A[k] = nro
        dimA += 1

    return dimA

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

    return None

# Programa Principal

DIM_FISICA = 10
A = np.empty(DIM_FISICA, dtype=int)
dimLogica = cargarVector(A)
ordenarVector(A,dimLogica)

nro = int(input("Ingrese el nro a insertar (0-Fin): "))
while nro != 0 and dimLogica < DIM_FISICA:
    dimLogica = insertarVector(A, dimLogica, nro)
    mostrarVector(A,dimLogica)
    nro = int(input("\nIngrese el nro a insertar (0-Fin): "))

if dimLogica == DIM_FISICA:
    print("No hay mas lugar en el arreglo")
