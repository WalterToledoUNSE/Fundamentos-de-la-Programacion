import numpy as np
# Indicar el mayor elemento de un vector de números enteros.

# Definición de Módulos
def buscarMayorValor(v, dim):
    mayor = v[0]
    for i in range(dim):
        if v[i]>mayor:
            mayor = v[i]
    return mayor

# Programa Principal
DIMV = 50
vector = np.empty(DIMV, dtype=int)
dim = int(input("Ingrese la cantidad de elementos del vector: "))

for i in range(dim):
    valor = int(input("Ingrese un valor: "))
    vector[i] = valor

may = buscarMayorValor(vector,dim)
print("El mayor elemento del vector es:",may)