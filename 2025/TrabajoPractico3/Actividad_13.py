import numpy as np

DIMFILA = 8
DIMCOLUMNA = 5

dimLogFila = 0

equipos = np.empty([DIMFILA,DIMCOLUMNA],dtype=int)
equipos = np.array([
    [10,11,1,2025,1400],
    [20,21,2,2025,2400],
    [50,11,1,2024,5400],
    [30,31,2,2023,3400],
    [ 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0],
])
dimLogFila = 4

print(" La matriz original")
for i in range(dimLogFila):
    for j in range(DIMCOLUMNA):
        print(equipos[i][j],end=" ")
    print(" ")

i = 0
while i < 2:
    codigoEquipo = int(input("Ingrese código de equipo: "))
    codigoLaboratorio = int(input("Ingrese código de laboratorio: "))
    cantidad = int(input("Ingrese la cantidad de equipos: "))
    anio = int(input("Ingrese año de adquisición: "))
    valor = int(input("Ingrese el valor del equipo: "))
    print("")

    equipos[dimLogFila][0] = codigoEquipo
    equipos[dimLogFila][1] = codigoLaboratorio
    equipos[dimLogFila][2] = cantidad
    equipos[dimLogFila][3] = anio
    equipos[dimLogFila][4] = valor

    dimLogFila = dimLogFila + 1

    i = i + 1

print(" La matriz actualizada")
for i in range(dimLogFila):
    for j in range(DIMCOLUMNA):
        print(equipos[i][j],end=" ")
    print(" ")