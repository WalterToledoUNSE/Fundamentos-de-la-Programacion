# Actividad 4
# Cargar un vector P con 10 números positivos ingresados por el usuario.
# Si el valor ingresado es negativo, pedirlo que se ingrese nuevamente. Imprimir el vector.

import numpy as np

DIM = 10
vector = np.empty(DIM, dtype=int)

i = 0
while i < DIM:
    numero = int(input("Ingrese un número:"))
    while numero <= 0:
        print("El número ingresado no es positivo")
        numero = int(input("Ingrese un nuevo número:"))
    vector[i] = numero
    i = i + 1

print("El vector generado es el siguiente:")
for i in range(0,DIM):
    print(vector[i], end=" ")
print("")