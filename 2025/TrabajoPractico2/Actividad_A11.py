# Se tiene un vector COD de 50 elementos que contiene los códigos de productos registrados en un depósito.
# A partir del ingreso de un código X, se pide:
# Verificar si el producto con código X está registrado.
# • En caso afirmativo, indicar la posición que ocupa dentro del vector.
# • En caso negativo, informar que no se encuentra registrado.

import random as rd
import numpy as np

N = 50
COD = np.empty(N,dtype=int)

# Se carga el vector con valores aleatorios entre 1 y 999
for i in range(N):
    COD[i] = rd.randint(1, 999)

print("El vector original es el siguiente:")
for i in range(N):
    print(COD[i], end=" ")

print("\n")
codigoX = int(input("Ingrese un número:"))
posicion = -1
existe = False
i = 0
while i < N and not existe:
    if COD[i] == codigoX:
        posicion = i
        existe = True
    i+=1

if existe:
    print("El número ingresado existe en la posición ",posicion)
else:
    print("El número ingresado no existe")
