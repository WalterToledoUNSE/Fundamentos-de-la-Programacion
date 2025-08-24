# La Facultad realizó una encuesta a 95 estudiantes sobre cuántas asignaturas
# habían aprobado en el último cuatrimestre. Los resultados se encuentran
# almacenados en el vector MAT, donde cada elemento representa la cantidad de
# materias aprobadas por un estudiante. Se pide: Ingresar un número X (cantidad de materias)
# e imprimir cuántos estudiantes aprobaron exactamente X materias.

import random as rd
import numpy as np

N = 95
MAT = np.empty(N,dtype=int)

# Se carga el vector con valores aleatorios entre 1 y 15
for i in range(N):
    MAT[i] = rd.randint(1, 12)
    
print("El vector original es el siguiente:")
for i in range(N):
    print(MAT[i], end=" ")

print("\n")
numeroX = int(input("Ingrese un número:"))
cantidad = 0
for i in range(N):
    if MAT[i] == numeroX:
       cantidad+=1

print("La cantidad de alumnos que aprobaron",numeroX,"materias en el cuatrimestre es de",cantidad)
