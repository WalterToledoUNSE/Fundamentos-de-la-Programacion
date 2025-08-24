import numpy as np

FILAS = 3
COLUMNAS = 3
#declaro la matriz
matriz = np.empty((FILAS,COLUMNAS),dtype=int)

#carga estática
# matriz2 = np.array([[1,2,3],
#                    [4,5,6]
# ])

#carga dinámica con WHILE
#i = 0
#while i < FILAS:
#    j = 0
#    while j < COLUMNAS:
#        matriz[i,j] = int(input("Ingrese un nro: "))
#        j += 1
#    i += 1

#carga dinámica con FOR
for i in range(0,FILAS):
    for j in range(0,COLUMNAS):
        matriz[i][j] = int(input("Ingrese un nro: "))

#mostrar MATRIZ
print("La matriz ingresada es la siguiente:")
for i in range(0,FILAS):
    for j in range(0,COLUMNAS):
        print(matriz[i][j], end=" ")
    print("")
