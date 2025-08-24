# Actividad 1
# Generar un vector con el mayor valor de cada uno de los 10 pares de números ingresados.
# (se ingresan pares de números con valores distintos).

import numpy as np

DIM = 5
vector = np.empty(DIM, dtype=int)

i = 0
while i < DIM:
    numero1 = int(input("Ingrese el primer número:"))
    numero2 = int(input("Ingrese el segundo número:"))
    if numero1 != numero2: # Si los número son iguales, no se considera para ser guardado en el vector
        if numero1 > numero2:
            vector[i] = numero1
        else:
            vector[i] = numero2
        i = i + 1

print("El vector generado es el siguiente:")
for i in range(0,DIM):
    print(vector[i], end=" ")
print("")