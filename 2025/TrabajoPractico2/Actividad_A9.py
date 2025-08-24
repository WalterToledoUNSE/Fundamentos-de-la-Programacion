# Dado un vector T (12) que contiene las temperaturas promedio de cada uno
# de los meses del año. Se pide imprimir la menor temperatura de la estación
# invierno y la mayor temperatura de la estación primavera.

import numpy as np

N = 12
T = np.empty(N,dtype=int)
T = np.array([31,31,10,29,28,24,18,5,46,40,48,30])

print("El vector original es el siguiente:")
for i in range(N):
    print(T[i], end=" ")

inicioInvierno = 5
inicioPrimavera = 8
menor = 100
mayor = 0
# range(inicio, fin, incremento): Genera una secuencia desde "inicio" hasta "fin" - 1, con un incremento de "incremento".
# Por ejemplo, range(1, 10, 2) generará 1, 3, 5, 7, 9.
for i in range(inicioInvierno, N, 1):
    if i > 7: # Condicion para saber en que estacion me encuentro
        # Estacion Primavera
        if i == inicioPrimavera: # Condicion para establecer el primer valor como mayor
            mayor = T[i]
        else:
            if T[i] > mayor:
                mayor = T[i]
    else:
        # Estacion Invierno
        if i == inicioInvierno: # Condicion para establecer el primer valor como menor
            menor = T[i]
        else:
            if T[i] < menor:
                menor = T[i]

print("\n")
print("La menor temperatura de invierno es:", menor)
print("La mayor temperatura de primavera es:", mayor)