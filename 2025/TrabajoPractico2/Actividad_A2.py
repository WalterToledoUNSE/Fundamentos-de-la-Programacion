# Actividad 2
# Generar un vector con la Categoría de cada uno de los N alumnos de Lógica I.
# La categoría se establece con el cálculo del promedio obtenido por cada alumno
# luego de rendir tres parciales, y teniendo en consideración la siguiente tabla:
#           |Nota Promedio|Categoría|
#           |   0 a 6     |   “D”   |
#           |   6 a 8     |   “A”   |
#           |   8 a 10    |   “P”   |

import numpy as np

DIM = 100
vector = np.empty(DIM, dtype='U1')
n = int(input("Ingrese la cantidad de alumnos de la asignatura lógica I:"))

i = 0
while i < n:
    # PENDIENTE: Agregar validación de notas que debe estar entre 0 y 100
    nota1 = float(input("Ingrese la primera nota:"))
    nota2 = float(input("Ingrese la segunda nota:"))
    nota3 = float(input("Ingrese la tercera nota:"))
    promedio = (nota1 + nota2 + nota3)/3
    print("El promedio de notas es %.2f"%promedio)
    if promedio >= 0 and promedio < 6:
        vector[i] = 'D'
    else:
        if promedio >= 6 and promedio < 8:
            vector[i] = 'A'
        else:
            if promedio >= 8 and promedio <= 10:
                vector[i] = 'P'
            else:
                vector[i] = 'N' # Esta situación no debe ocurrir si se valida los datos de entrada
    print(" ")
    i = i + 1

print("El vector generado es el siguiente:")
for i in range(0,n):
    print(vector[i], end=" ")
print("")