# Dado el vector E(X) se pide permutar sus elementos de la siguiente manera:
# A (1) con A(X), A (2) con A (X-1), A (3) con A (X-2) y así sucesivamente.
# Mostrar el vector sin elementos permutados y el vector con los elementos permutados.

import numpy as np

N = 9
A = np.empty(N,dtype=int)
A = np.array([10,20,30,40,50,60,70,80,90])

print("El vector original es el siguiente:")
for i in range(N):
    print(A[i], end=" ")

ultimo = N-1 # Se considera la ultima posición el valor N-1 porque se comienza en 0 las posiciones (indice)
for i in range(N//2): # Se recorre la mitad del vector para respectar el orden
    aux = A[ultimo - i]
    A[ultimo - i] = A[i]
    A[i] = aux

print("\n") # Esto es un salto de línes
print("El vector permutado es el siguiente:")
for i in range(N):
    print(A[i], end=" ")