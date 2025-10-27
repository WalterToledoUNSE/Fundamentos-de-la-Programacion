# Ordenar la matriz por código de Producto de forma descendente
# e imprimirla.

import numpy as np

DIMFILA = 8
DIMCOLUMNA = 6

dimLogFila = 0

stock = np.empty([DIMFILA,DIMCOLUMNA],dtype=int)
stock = np.array([
    [10,11,12,13,14,15],
    [20,21,22,23,24,25],
    [50,51,52,53,54,55],
    [30,31,32,33,34,35],
    [ 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0],
])
dimLogFila = 4

print(" La matriz original")
for i in range(dimLogFila):
    for j in range(DIMCOLUMNA):
        print(stock[i][j],end=" ")
    print(" ")

i = 0
while i < dimLogFila - 1:
    p = i
    j = i + 1
    while j < dimLogFila:
        if stock[j][0] > stock[p][0]:
            p = j
        j = j + 1
    c = 0
    while c < DIMCOLUMNA:
        aux = stock[p][c]
        stock[p][c] = stock[i][c]
        stock[i][c] = aux
        c = c + 1
    i = i + 1

print("\n La matriz ordenada")
for i in range(dimLogFila):
    for j in range(DIMCOLUMNA):
        print(stock[i][j],end=" ")
    print(" ")

print(" ")
codigoProducto = int(input("Ingresar un código de producto:"))
band = False
i = 0
while i < dimLogFila and not band:
    if stock[i][0] == codigoProducto:
        band = True
    i = i + 1

if band:
    print("El código ingresado ya existe en el stock!!!")
else:
    i = 0
    band = False
    while i < dimLogFila and not band:
        if codigoProducto > stock[i][0]:
            j = dimLogFila
            while j >= i:
                c = 0
                while c < DIMCOLUMNA:
                    stock[j+1][c] = stock[j][c]
                    c = c + 1
                j = j - 1
            stock[i][0] = codigoProducto
            stock[i][1] = 0
            stock[i][2] = 0
            stock[i][3] = 0
            stock[i][4] = 0
            stock[i][5] = 0
            dimLogFila = dimLogFila + 1
            band = True
        else:
            i = i + 1
    if not band:
        stock[i][0] = codigoProducto
        stock[i][1] = 0
        stock[i][2] = 0
        stock[i][3] = 0
        stock[i][4] = 0
        stock[i][5] = 0
        dimLogFila = dimLogFila + 1

    print("\n La matriz actualizada")
    for i in range(dimLogFila):
        for j in range(DIMCOLUMNA):
            print(stock[i][j], end=" ")
        print(" ")






