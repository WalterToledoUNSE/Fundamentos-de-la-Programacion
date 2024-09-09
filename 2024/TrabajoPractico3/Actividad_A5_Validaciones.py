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
DIM_FISICA = 50
vector = np.empty(DIM_FISICA, dtype=int)
dimLogica = 0
valido = False
# Se genera un ciclo para validar la dimensión lógica del vector
while not valido:
    dimLogica = int(input("Ingrese la cantidad de elementos del vector: "))
    if dimLogica > 0 and dimLogica<DIM_FISICA:
        valido = True
    else:
        print("La dimensión no debe ser 0 ni mayor a ",DIM_FISICA)


for i in range(dimLogica):
    valor = int(input("Ingrese un valor: "))
    vector[i] = valor

may = buscarMayorValor(vector,dimLogica)
print("El mayor elemento del vector es:",may)