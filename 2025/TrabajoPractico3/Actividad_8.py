# Una farmacia registra en una matriz REMEDIOS (Nx6) los siguientes datos:
# Código de Vendedor, Código de laboratorio (1- Bago, 2- Johnson, 3- Bayer),
# importe de las ventas vendedor 1, importe de las ventas vendedor 2,
# importe de las ventas vendedor 3, importe de las ventas vendedor 4
# A. Imprimir los datos de un determinado remedio,
# B. Generar un vector con los códigos de Remedios que pertenezcan
#    a un determinado Laboratorio
# C. Calcular e imprimir el código de remedio de mayor venta.

import numpy as np

DIMF = 1000 # Dimensión Física
DIMC = 6
#declaro la matriz
A = np.empty((DIMF,DIMC),dtype=int)
dimLogica = 6

A = np.array([
    [100,1,27,98,53,56],
    [200,2,34,17,13,65],
    [300,1,99,85,68,24],
    [400,2,50,88,88,77],
    [500,1,76,24,96,63],
    [600,3,86,34,86,78]
])
vectorB = np.empty(DIMF, dtype=int)
dimLogVectorB = 0
print(A)

# A. Imprimir los datos de un determinado remedio
codigoRemedio = int(input("Ingrese el código del remedio:"))
for i in range(dimLogica):
    if A[i][0] == codigoRemedio:
        print(" ")
        print("El código del remedio es:",codigoRemedio)
        print("El código del laboratorio es:",A[i][1])
        vendedor = 2
        while vendedor < DIMC:
            numVendedor = vendedor-1
            print("Ventas del vendedor",numVendedor,"es de:",A[i][vendedor])
            vendedor+=1
print("\n")

# B. Generar un vector con los códigos de Remedios que pertenezcan a un determinado Laboratorio
codigoLaboratorio = int(input("Ingrese el código del laboratorio:"))
for i in range(dimLogica):
    if A[i][1] == codigoLaboratorio:
        vectorB[dimLogVectorB] = A[i][0]
        dimLogVectorB+=1
print("El vector con los productos del laboratorio",codigoLaboratorio,"son:")
for i in range(dimLogVectorB):
    print(vectorB[i],end=" ")