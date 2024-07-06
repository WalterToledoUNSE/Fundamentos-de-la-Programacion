import numpy as np




# ENUNCIADO
# Dadas N palabras, determinar la palabra que tiene mayor cantidad de vocales.

N = int(input("Ingrese la cantidad de palabras: "))
mayor = 0
palabraMayor = ""
for i in range(N):
    palabra = input("Ingrese una palabra: ")
    cantidad = 0
    # Ciclo para recorrer todas las letras de las palabras.
    for letra in palabra:
        # Se convierte la letra a minusculas
        if(letra.lower() in 'aeiou'):
            cantidad = cantidad + 1
    if cantidad > mayor:
        mayor = cantidad
        palabraMayor = palabra
# Si no existen vocales en las palabras ingresadas se informa tal situación.
if mayor > 0:
    print("La palabra que tiene mayor cantidad de vocales es",palabraMayor, "y tiene", mayor,"vocal(es)")
else:
    print("Las palabras ingresadas no tienen vocales.")