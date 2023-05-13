# 3) Dada una serie de números, cuyo final viene dado por el ingreso
# del cero, que representan las edades un grupo de estudiantes, mostrar:
# a) El porcentaje de edades iguales a 19 y la mayor edad de las
# edades superiores a 19.
# b) La categoría a la que pertenece cada alumno teniendo en cuenta:
# Edad                 Categoría
# Entre 15 y 18 años      I
# Entre 19 y 22 años      II
# Entre 23 y 25 años      III
# c) La edad media de este grupo de alumnos.

c = 0; cantidadEdad19 = 0; mayor = 0;  porcentaje = 0; sum = 0; media = 0
edad = int(input("Ingrese la edad del alumno: "))
while edad > 0:
    c = c + 1
    # Punto a
    if edad == 19:
        cantidadEdad19 = cantidadEdad19 + 1
    else:
        if edad > 19:
            if edad > mayor:
                mayor = edad
    # Punto b
    if edad >= 15 and edad <= 18:
        print("La categoria correspondiente es I")
    else:
        if edad >= 19 and edad <= 22:
            print("La categoria correspondiente es II")
        elif edad >= 23 and edad <= 25:
                print("La categoria correspondiente es III")
    sum = sum + edad # Punto c
    edad = int(input("Ingrese la edad del alumno: "))
if c > 0:
    porcentaje = (cantidadEdad19 / c) * 100
print("\n---------------------------------------------------------")
print("El porcentaje de edades iguales a 19 es de: %.2f"%porcentaje,"(%)")
print("---------------------------------------------------------")
print("La mayor edad de las edades superiores a 19 es de:",mayor)
if c > 0:
    media = sum / c
print("---------------------------------------------------------")
print("La edad media de este grupo de alumnos: ",media)
print("---------------------------------------------------------")