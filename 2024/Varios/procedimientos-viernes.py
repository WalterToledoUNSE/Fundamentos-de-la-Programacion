import numpy as np
import random

## Procedimiento que retorna mas de un valor
def determinarMayorMenor(v, d):
    may = -999
    men = 999
    for i in range(d):
        if v[i] > may:
            may = v[i]
        if v[i] < men:
            men = v[i]
    return may,men

## Procedimiento sin retorno
def mostrarMayorMenor(v, d):
    may = -999
    men = 999
    for i in range(d):
        if v[i] > may:
            may = v[i]
        if v[i] < men:
            men = v[i]
    print("El mayor valor es",may,"y el menor es", men)
    return None

## Cargar vector random

def cargarRandom(v):
    dim = int(input("Ingrese la cantidad de elementos del vector: "))
    for i in range(dim):
        v[i] = random.randrange(0, 100)
    return dim

def mostrarVector(v,d):
    for i in range(d):
        print(v[i], end=" ")
    print("")
    return None

## Porgrama principal
vector = np.empty(100, dtype=int)
DIM = cargarRandom(vector)
mostrarVector(vector,DIM)
mayor, menor = determinarMayorMenor(vector,DIM)
print("El mayor valor es",mayor,"y el menor es", menor)
