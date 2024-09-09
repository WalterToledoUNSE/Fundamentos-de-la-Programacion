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
x = int(input("Ingrese el número a buscar en el vector: "))

pos = buscarNumero(vector,dimLogica, x)
if pos > -1:
    print("El número",x,"existe en la posición ",pos,"del vector")
else:
    print("El número ingresado no existe")