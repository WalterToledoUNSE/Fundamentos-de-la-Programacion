# Una zapatería tiene una planilla con los ingresos obtenidos
# por cada uno de sus N empleados, en la venta de 5 productos. Se pide:
# 1. Generar la estructura de datos que permita almacenar los ingresos.
# 2. Mostrar para cada producto la mayor venta.
# 3. Mostrar para un determinado vendedor el promedio de sus ventas.


import numpy as np

DIMF = 1000 # Dimensión Física
DIMC = 5

#declaro la matriz
A = np.empty((DIMF,DIMC),dtype=int)
dimLogica = 6

A = np.array([
    [41,72,27,98,53],
    [55,49,34,17,13],
    [82,67,99,85,68],
    [37,62,50,88,88],
    [51,15,76,24,96],
    [61,25,86,34,86]
])

# 2. Mostrar para cada producto la mayor venta.
for j in range(DIMC):
    # mayor = A[0][j] Esto es otra opción
    for i in range(dimLogica):
        if i == 0:
            mayor = A[i][j]
        else:
            if A[i][j] > mayor:
                mayor = A[i][j]
    producto = j + 1
    print("La mayor venta del producto", producto,"es de:",mayor)
print("\n")

# 3. Mostrar para un determinado vendedor el promedio de sus ventas.
codV = int(input("Ingrese el código del vendedor:"))
codigoVendedor = codV - 1
existe = False
for i in range(dimLogica):
    if(i == codigoVendedor):
        existe = True
        suma = 0
        for j in range(DIMC):
            suma = suma + A[i][j]
        promedio = suma / DIMC
        print("El promedio de ventas, del vendedor", codV,"es de: %.2f"%promedio)
        # print("El promedio de ventas, del vendedor", codV,"es de:",promedio)
if not existe:
    print("El código ingresado no existe")