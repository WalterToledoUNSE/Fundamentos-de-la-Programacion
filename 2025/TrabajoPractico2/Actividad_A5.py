# Actividad 5
# Se leen una serie de números que representan las edades de un grupo de estudiantes;
# cuyo final está dado por el ingreso de un cero o hasta alcanzar el tamaño máximo del
# vector (20 elementos). Realizar la carga de las edades en el vector EDADES e imprimir el vector resultante.
# Con el vector generado, se pide calcular e imprimir:
# a) El porcentaje de edades iguales a 19 y la mayor edad de las edades superiores a 19.
# b) La categoría a la que pertenece cada alumno teniendo en cuenta:
#   |        Edad        |  Categoria
#   |Entre 15 y 18 años  |      I
#   |Entre 19 y 22 años  |     II
#   |Entre 23 y 25 años  |    III
# c) La edad media de este grupo de alumnos.

import numpy as np

DIM = 5
edades = np.empty(DIM, dtype=int)

# Se realiza la carga de datos en el vector
i = 0
bandera = False
while i < DIM and not bandera:
    edad = int(input("Ingrese una edad:"))
    if edad != 0:
        edades[i] = edad
        i = i + 1
    else:
        bandera = True

# Se muestran los datos del vector
dim = i
print("El edades generado es el siguiente:")
for i in range(0,dim):
    print(edades[i], end=" ")
print("")

may = 0
sum = 0
edadIgual19 = 0
for i in range(0,dim):
    # a) El porcentaje de edades iguales a 19 y la mayor edad de las edades superiores a 19.
    if edades[i] >= 19:
        if edades[i] > 19:
            if i == 0:
                may = edades[i]
            else:
                if edades[i] > may:
                    may = edades[i]
        else:
            edadIgual19 = edadIgual19 + 1
    # b) La categoría a la que pertenece cada alumno
    if edades[i] >= 15 and edades[i] <= 18:
        print("El edad corresponde a la categoria I")
    else:
        if edades[i] > 18 and edades[i] <= 22:
            print("El edad corresponde a la categoria II")
        else:
            if edades[i] > 22 and edades[i] <= 25:
                print("El edad corresponde a la categoria III")

    sum = sum + edades[i] # c) La edad media de este grupo de alumnos.

promedio = sum / dim
print("El promedio de edades del grupo es de: %.2f"%promedio)
porcentaje = (edadIgual19 / dim) * 100
print("El porcentaje de alumnas con edad igual a 19 años es de: %.2f"%porcentaje,"(%)")

