import numpy as np
# Dado un número X, indicar la posición en la que se encuentra dentro de un vector.

# Definición de Módulos
def buscarNumero(v, dim, numero):
    posicion = -1
    for i in range(dim):
        if v[i] == numero:
            posicion = i
    return posicion

# Programa Principal
DIMV = 50
vector = np.empty(DIMV, dtype=int)
dim = int(input("Ingrese la cantidad de elementos del vector: "))

for i in range(dim):
    valor = int(input("Ingrese un valor: "))
    vector[i] = valor
x = int(input("Ingrese el número a buscar en el vector: "))

pos = buscarNumero(vector,dim, x)
if pos > -1:
    print("El número",x,"existe en la posición ",pos,"del vector")
else:
    print("El número ingresado no existe")