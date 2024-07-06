import numpy as np

DIM_F = 10
DIM_C = 4
n = 5

s = np.empty((DIM_F, DIM_C),dtype=int)
s = np.array([
    [134, 1, 49675, 32544],
    [340, 2, 80133, 41122],
    [108, 1, 38769, 45890],
    [180, 3, 52769, 90890],
    [210, 2, 90769, 60890],
])

print("#######################################################################################################")
print("Los datos ingresados son los siguientes:")

for i in range(0,n):
    for j in range(0,DIM_C):
        print(s[i][j],end=" ")
    print(" ")
print(" ")

# TODO:  PROBLEMA 1
# TODO:  Imprimir la información de todos los medidores que
# TODO:  pertenezcan a un determinado código de Barrio.
# TODO:  Al final imprimir el promedio de consumo de cada semestre.

sum1 = 0
sum2 = 0
c = 0
print("#######################################################################################################")
codigoBarrio = int(input("Por favor ingrese un código de barrio: "))
print(" ")
for i in range(0,n):
    if s[i][1] == codigoBarrio:
        print("Medidor: ", s[i][0])
        print("\tConsumo 1 semestre es: ",s[i][2])
        print("\tConsumo 2 semestre es: ",s[i][3])
        print(" ")
        sum1 = sum1 + s[i][2]
        sum2 = sum2 + s[i][3]
        c += 1

if(c > 0):
    promedio1 = sum1/c
    promedio2 = sum2/c
    print("Los consumos promedio anual son los siguientes:")
    print("\t1 Semestre es: ", promedio1)
    print("\t2 semestre es: ", promedio2)
else:
    print("No existen medidores para el código de barrio ingresado")
print(" ")

# TODO:  Generar un vector con los números de medidores de los clientes
# TODO:  que tengan un consumo en el primer semestre mayor a 80000 o con
# TODO:  un consumo en el segundo semestre mayor a 90000. Imprimir el
# TODO:  vector generado.

print("#######################################################################################################")
v = np.empty(n, dtype=int)
dimV = 0
for i in range(0,n):
    if s[i][2] > 80000 or s[i][3] > 90000:
        v[dimV] = s[i][0]
        dimV = dimV + 1
if dimV > 0:
    print("Los siguientes medidores registraron consumos superiores a 80.000 o 90.000:")
    for i in range(0,dimV):
        print(" ", v[i], end=" ")
else:
    print("No existen medidores con consumos superiores a 80.000 o 90.000.")
print(" ")

# TODO:   Imprimir el número de medidor y el código de barrio
# TODO:   del cliente que tenga el mayor consumo promedio

numeroMedidorAux = 0
codigoBarrioAux = 0
mayor = 0
for i in range(0,n):
    promedio = (s[i][2] + s[i][3]) / 2
    if i == 0:
        numeroMedidorAux = s[i][0]
        codigoBarrioAux = s[i][1]
        mayor = promedio
    else:
        if promedio > mayor:
            numeroMedidorAux = s[i][0]
            codigoBarrioAux = s[i][1]
            mayor = promedio
print("#######################################################################################################")
print("El medidor del cliente con el mayor consumo promedio es",numeroMedidorAux,"y corresponde al código de barrio",codigoBarrioAux)
# print("El código barrio del cliente con el mayor consumo promedio es: ",codigoBarrioAux)
print(" ")

print("#######################################################################################################")
print("Se realizará el ordenamiento del vector...")
for i in range(0, dimV):
    print(" ", v[i], end=" ")

i = dimV
b = 1
while b != 0:
    b = 0
    j = 0
    while j<i-1:
        # AQUI en el if debo cambiar el signo si quiero que el ordenamiento sea ascendente o descendente
        if v[j] < v[j+1]:
            aux = v[j]
            v[j] = v[j+1]
            v[j+1] = aux
            b = 1
        j += 1
    i -= 1

print(" ")
print("El vector resultante es el siguiente...")

# muestro vector resultante
for i in range(dimV):
    print(v[i], end=" ")
print(" ")
print("#######################################################################################################")


nro = int(input("Ingrese número de medidor a insertar (0 para finalizar): "))
while nro != 0 and dimV < n: # dimensión física del vector es de 5 elementos
    b = 0
    k = 0
    print("VALOR DE DIMV: ",dimV)
    while k < dimV and b == 0:
        if nro > v[k]:
            j=dimV-1
            while j >= k:
                v[j+1] = v[j]
                j = j-1
            v[k] = nro
            dimV += 1
            b = 1
        else:
            k += 1
    if b == 0:
        v[k] = nro
        dimV += 1

    for i in range(dimV):
        print(v[i], end=" ")
    print("")
    nro = int(input("Ingrese número de medidor a insertar (0 para finalizar): "))
if dimV == n:
    print("No hay mas lugar")
print(" ")

print("#######################################################################################################")
x = int(input("Ingrese el número del medidor que desea eliminar: "))
i = 0
b = 0
while i < dimV and b == 0:
    if v[i] == x:
        j = i
        b = 1
        while j < dimV-1:
            v[j] = v[j+1]
            j = j + 1
        dimV -= 1
    else:
        i += 1
print(" ")
if(b == 0):
    print("El número de medidor ingresado no existe.")
else:
    print("El número de medidor ingresado fue eliminado exitosamente")
    for i in range(0, dimV):
        print(" ", v[i],end=" ")
print("#######################################################################################################")
