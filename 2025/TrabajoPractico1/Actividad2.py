edad = int(input("Ingrese la edad: "))
cantEdad = 0
may = 0
sum = 0
c = 0
porc = 0
while edad > 0:
    if edad == 19:
        cantEdad = cantEdad + 1
    else:
        if edad > 19:
            if edad > may:
                may = edad
    if edad >= 15 and edad <= 18:
        print(" La edad corresponde a la categoria I")
    else:
        if edad >= 19 and edad <= 22:
            print(" La edad corresponde a la categoria II")
        else:
            if edad >= 23 and edad <= 25:
                print(" La edad corresponde a la categoria III")
    sum = sum + edad
    c = c + 1
    edad = int(input("Ingrese la edad: "))
if cantEdad > 0:
    porc = (cantEdad / c) * 100
print("El porcentaje de edades es de: ",porc)
if may > 0:
    print("La mayor edad de 19 años es: ",may)
if c > 0:
    prom = sum / c
print("El promedio de edades ingresadas es de: ",prom)