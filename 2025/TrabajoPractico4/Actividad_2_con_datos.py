# 2. Una empresa guarda en un arreglo tipo registro  EMPLEADOS[N] los siguientes datos
#    de sus empleados: DNI, Apellido, Sueldo, Estado (Activo/Inactivo)
# Se pide elaborar un diagrama de flujo que permita:
# a) Añadir un nuevo empleado al final del vector (si hay espacio).
# b) Dar de baja lógica a un determinado empleado (cambiar a Inactivo).

import numpy as np
import random as rd

# Definición de la estructura TAlumnos
TEmpleados = np.dtype([
    ('dni',int),
    ('apellido','U25'),
    ('sueldo',float),
    ('estado',bool) # True es para Activo y False para Inactivo
])

DIM = 10
dimLogica = rd.randint(1, DIM+5) # Se genera una valor aleatoria para la dimensión lógica
if dimLogica > DIM: # Si el valor aleatorio es mayor a la dimensión física, se iguala la dimensión lógica con la física
    dimLogica = DIM
dimLogica = 9

empleados = np.empty(DIM,dtype=TEmpleados) # Se genera el arreglo de tipo TEmpleados

for i in range(dimLogica):
    # Carga aleatoria de datos:
    empleados[i]["dni"] = rd.randint(20000000, 40000000) # Se genera un número entero aleatorio entre 20.000.000 y 40.000.000
    empleados[i]["apellido"] = "Empleado"+str(i+100) # Se genera el apellido genérico del empleado
    empleados[i]["sueldo"] = rd.uniform(100000, 999999) # Se genera un número con decimales aleatorio entre 100.000 y 999.999
    empleados[i]["estado"] = rd.choice([True, False]) # Se genera un valor aleatorio que puede ser True o False


# Se muestra los resultados del arreglo
print("************************************************************")
print("*                   Listado de Empleados                   *")
print("************************************************************")
print("#    DNI \t\t Apellido \t\t\tSueldo\t\t\tEstado") # El simbolo \t es una tabulación
for i in range(dimLogica):
    # Se analiza el campo estado para mostrar el texto "Habilitado" o "Inhabilitado" en lugar de True o False
    if(empleados[i]['estado']):
        estado = 'Habilitado'
    else:
        estado = 'Inhabilitado'
    print((i+1),".",empleados[i]["dni"],"\t",empleados[i]["apellido"],"\t $ %.2f"%empleados[i]["sueldo"], "\t",estado)
    # La expresión %.2f es para mostrar dos decimales en el sueldo

# ITEM A
if dimLogica < DIM:
    print("Ingrese los datos del empleado")
    dni = int(input("Ingrese el DNI del empleado (0 para cancelar): "))
    while dni > 0 and dimLogica < DIM:

        apellido = input("Ingrese el apellido del empleado: ")
        sueldo = float(input("Ingrese el sueldo del empleado: "))

        empleados[dimLogica]["dni"] = dni
        empleados[dimLogica]["apellido"] = apellido
        empleados[dimLogica]["sueldo"] = sueldo
        empleados[dimLogica]["estado"] = True
        dimLogica = dimLogica + 1

        if dimLogica == DIM:
            print("\nEl arreglo esta lleno!!!\n")
        else:
            print(" ")  # Genera un salto de línea en la terminal
            dni = int(input("Ingrese el DNI del empleado (0 para cancelar): "))
else:
    print("\nNo hay espacio para mas elementos.\n")


# Se muestra los resultados del arreglo
print("************************************************************")
print("*                   Listado de Empleados                   *")
print("************************************************************")
print("#    DNI \t\t Apellido \t\t\tSueldo\t\t\tEstado")
for i in range(dimLogica):
    if(empleados[i]['estado']):
        estado = 'Habilitado'
    else:
        estado = 'Inhabilitado'
    print((i+1),".",empleados[i]["dni"],"\t",empleados[i]["apellido"],"\t $ %.2f"%empleados[i]["sueldo"], "\t",estado)

# ITEM B
print(" ")
dni = int(input("Ingrese el DNI del empleado a dar de baja: "))
i = 0
existe = False
while i < dimLogica and not existe:
    if empleados[i]["dni"] == dni:
        empleados[i]["estado"] = False
        existe = True
    i+=1
if existe:
    print("El empleado fue inhabilitado")
else:
    print("No existe empleado con el DNI ingresado")