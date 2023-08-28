# Para una cadena de caracteres determinar y mostrar la cantidad de vocales que tiene la cadena.

# Definición de Módulos
def contarVocales(v, dim):
    vocales = 0
    for i in range(dim):
        vocal = v[i].upper()
        if vocal == "A" or vocal == "E" or vocal == "I" or vocal == "O" or vocal == "U":
            vocales+=1
    return vocales

# Programa Principal
mje = input("Ingrese una cadena de texto: ")
dim = len(mje)

cantidadVocales = contarVocales(mje, dim)
print("La cantidad de vocales en el string ingresado es de:",cantidadVocales)