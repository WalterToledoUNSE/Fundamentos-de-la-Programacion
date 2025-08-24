# Dado el vector X, el cual contiene la letra inicial del apellido de N alumnos , se pide imprimir:
# a) “Creciente”, si el listado esta ordenado estrictamente creciente A(0) < A(1) < A(2) <....< A(N-1).
# b) “Decreciente”, si el listado esta ordenado estrictamente decreciente A(0) > A(1) > A(2) >... > A(N-1).
# c) “Ninguna”, si no cumple con ninguna de los anteriores.

import numpy as np

N = 10
v = np.empty(N,dtype='U1')
# v = np.array(['a','b','c','d','e','f','g','h','i','j'])
v = np.array(['j','I','h','G','f','e','d','c','B','a'])

# Se convierte todas las letras a mayusculas
for i in range(N):
    v[i] = v[i].upper()

# Se utilizan las banderas para determinar el orden
esCreciente = True
esDecreciente = True

for i in range(N-1): # Se recorre hasta el penultimo elemento
    if v[i] > v[i + 1]:
        esCreciente = False
    if v[i] < v[i + 1]:
        esDecreciente = False

if esCreciente:
    print("Creciente")
elif esDecreciente:
    print("Decreciente")
else:
    print("Ninguna")