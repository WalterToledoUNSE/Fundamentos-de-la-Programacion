# Actividad 3
# Cargar un vector de 6 notas válidas entre 1 y 10. Validar que cada nota esté dentro del rango.

import numpy as np

DIM = 6
vector = np.empty(DIM, dtype=int)

i = 0
while i < DIM:
    nota = int(input("Ingrese una nota:"))
    while nota <= 0 or nota > 10:
        print("La nota debe estar comprendida entre 0 y 10")
        nota = int(input("Ingrese una nueva nota:"))
    vector[i] = nota
    i = i + 1

print("El vector generado es el siguiente:")
for i in range(0,DIM):
    print(vector[i], end=" ")
print("")