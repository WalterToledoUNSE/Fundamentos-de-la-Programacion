# 1.	Un instituto almacena los datos de sus alumnos en un arreglo tipo registro  ALUMNOS[N],
# con los campos: Legajo (entero),  Nombre (alfanumérico), Promedio (real)
# Se pide elaborar un diagrama de flujo que permita:
# a) Ingresar los datos de N alumnos.
# b) Imprimir el nombre del alumno con el promedio más alto.
# c) Para un determinado legajo ingresado por  teclado, si existe mostrar
#    todos los datos de ese alumno, caso contrario mostrar “Legajo Inexistente”.

import numpy as np
import random as rd

# Definición de la estructura TAlumnos
TAlumnos = np.dtype([
    ('legajo',int),
    ('nombre','U25'),
    ('promedio',float)
])

# ITEM A
N = 3 # Se define la dimensión física
alumnos = np.empty(N,dtype=TAlumnos) # Se genera el arreglo de tipo TAlumnos

for i in range(N):
    # Carga aleatoria de datos:
    alumnos[i]["legajo"] = rd.randint(1, 100) # Se genera un número entero aleatorio entre 1 y 100
    alumnos[i]["nombre"] = "Alumno_"+str(i+1) # Se genera el nombre de un alumno
    alumnos[i]["promedio"] = rd.uniform(1, 10) # Se genera un número con decimales aleatorio entre 1 y 10

# Se muestra los resultados del arreglo
print("***   Listado de Alumnos  ***")
print("Legajo \t  Nombre \t Promedio") # El simbolo \t es una tabulación
for i in range(N):
    print(" ",alumnos[i]["legajo"],"\t",alumnos[i]["nombre"],"\t   %.2f"%alumnos[i]["promedio"])
    # La expresión %.2f es para mostrar dos decimales. El número indica la cantidad de decimales

# ITEM B
mayorPromedio = 0
alumnoMayorPromedio = ''
for i in range(N):
    if i == 0:
        mayorPromedio = alumnos[i]['promedio']
        alumnoMayorPromedio = alumnos[i]['nombre']
    else:
        if alumnos[i]['promedio'] > mayorPromedio:
            mayorPromedio = alumnos[i]['promedio']
            alumnoMayorPromedio = alumnos[i]['nombre']
print(" ")
print("El alumno",alumnoMayorPromedio,"tiene el mayor promedio y es de %.2f"%mayorPromedio)

# ITEM C
print(" ")
nuevoLegajo = int(input("Ingrese el legajo del alumno a buscar: "))
existe = False
i = 0
while i < N and not existe:
    if alumnos[i]["legajo"] == nuevoLegajo:
        existe = True
    else:
        i = i + 1
if existe:
    print("** Datos del alumno **")
    print("Legajo: ",nuevoLegajo)
    print("Nombre: ", alumnos[i]["nombre"])
    print("Promedio: %.2f"%alumnos[i]["promedio"])
else:
    print("No existe el legajo ingresado")