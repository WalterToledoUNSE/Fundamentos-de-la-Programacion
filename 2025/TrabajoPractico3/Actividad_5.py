# Una empresa desea llevar el registro del rendimiento de
# sus 5 vendedores durante 4 semanas, en una matriz
# VENTAS (5x4). Se pide:
# 1. Cargar la matriz VENTAS(5x4)
# 2. Calcular e imprimir
#   a. Total de ventas por cada vendedor.
#   b. Total de ventas por cada semana.
#   c. Total general.

import numpy as np

FILAS = 5
COLUMNAS = 4
#declaro la matriz
ventas= np.empty((FILAS,COLUMNAS),dtype=int)

# Item 1 - Cargar la matriz VENTAS(5x4)
ventas = np.array([
    [41,72,27,98],
    [55,49,34,17],
    [82,67,99,85],
    [37,62,50,88],
    [51,15,76,24]
])

#   2.a. Total de ventas por cada vendedor.
for i in range(FILAS):
    totalVendedor = 0
    for j in range(COLUMNAS):
        totalVendedor = totalVendedor + ventas[i][j]
    vendedor = i+1
    print("El total vendido por el vendedor",vendedor,"es de:", totalVendedor)
print("\n")

#   2.b. Total de ventas por cada semana.
totalGeneral = 0 #   2.c. Total general.
for j in range(COLUMNAS):
    totalSemanal = 0
    for i in range(FILAS):
        totalSemanal = totalSemanal + ventas[i][j]
        totalGeneral = totalGeneral + ventas[i][j]
    semana = j+1
    print("El total vendido para la semana",semana,"es de:", totalSemanal)
print("\n")

print("El total general de ventas, es de:", totalGeneral)

