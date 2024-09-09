# Para una cadena de caracteres determinar y mostrar la cantidad de vocales que tiene la cadena.
import numpy as np


# Definición de Módulos
def contarVocales(v, dim):
    vocales = 0
    for i in range(dim):
        vocal = v[i].upper()
        if vocal == "A" or vocal == "E" or vocal == "I" or vocal == "O" or vocal == "U":
        # if vocal in('AEIOU'): #En lugar del los OR, se puede usar la sentencia "in"
            vocales+=1
    return vocales

# Programa Principal
mje = np.array(['h','o','L','a','_','m','U','n','d','O'])
dim = 10

cantidadVocales = contarVocales(mje, dim)
print("La cantidad de vocales en el string ingresado es de:",cantidadVocales)