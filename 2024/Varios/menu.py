import numpy as np
import random

def cargarRandom(v):
    dim = int(input("Ingrese la cantidad de elementos del vector: "))
    for i in range(dim):
        v[i] = random.randrange(100, 999)
    return dim

def ordenarVector(v,d):
    for i in range(0, d - 1):
        p = i
        for j in range(i + 1, d):
            if v[j] < v[p]:
                p = j
        w = v[p]
        v[p] = v[i]
        v[i] = w
    return None

def mostrarVector(v,d):
    for i in range(d):
        print(v[i], end= " ")
    print("")
    return None

def mostrarMenu():
    print("------- MI PROGRAMA -------")
    print("1- Cargar vector")
    print("2- Ordenar vector")
    print("3- Mostrar vector")
    print("4- Salir")
    return None

vector = np.empty(100, dtype=int)
salir = False
while not(salir):
    mostrarMenu()
    op = int(input("Seleccione una opción: "))
    if op == 1:
        dim = cargarRandom(vector)
    elif op == 2:
        ordenarVector(vector,dim)
    elif op == 3:
        mostrarVector(vector, dim)
    elif op == 4:
        salir = True
    else:
        print("Opción incorrecta")