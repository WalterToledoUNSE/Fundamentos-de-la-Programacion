# Cargar los datos en el vector. Ordenarlo en forma ascendente un vector A
# de 10 elementos, y luego mostrarlo ordenado.

import numpy as np

DIM_FISICA = 10
dim = 0
A = np.empty(DIM_FISICA, dtype=int)

def cargarDatos(A, dimF):
    dimensionLogica = 0
    for i in range(dimF):
        A[i] = int(input("Ingrese el valor: "))
        dimensionLogica +=1

    return dimensionLogica

def imprimirDatos(A, dimL):
    print("Los datos del vector son los siguientes:")
    for i in range(dimL):
        print(A[i], end=" ")
    return None

def ordenarDatos(A, dimL):
    i = 0
    while i < dimL - 1:
        p = i
        j = i + 1
        while j < dimL:
            # En este condicional el signo "< o >" determina el orden ascendente o descendente
            if A[j] > A[p]:
                p = j
            j += 1
        aux = A[p]
        A[p] = A[i]
        A[i] = aux
        i += 1
    return None

# Programa Principal
dim = cargarDatos(A,DIM_FISICA)
imprimirDatos(A,dim)
ordenarDatos(A,dim)
print(" ")
imprimirDatos(A,dim)