# 4. Una clínica médica gestiona información de sus pacientes en un arreglo tipo registro
#    PACIENTES[N] con: DNI, Nombre, Consultas[12] (arreglo con la cantidad de consultas en cada mes del año)
#    Se pide elaborar un diagrama de flujo que permita:
#       a) Para cada paciente, calcular e imprimir DNI y el total de consultas anuales.
#       b) Mostrar el DNI del paciente con mayor cantidad de consultas en el mes de agosto.

import numpy as np

DIMNOTAS = 12
DIM = 3
TPaciente = np.dtype([
    ("dni",int),
    ("nombre","U30"),
    ("consultas",(int,DIMNOTAS)) # Esta es la notación especial aceptada para definir un vector adentro de un registro
])

pacientes = np.empty(DIM,dtype=TPaciente)

for i in range(DIM):
    pacientes[i]["dni"] = int(input("Ingrese el DNI: "))
    pacientes[i]["nombre"] = input("Ingrese el nombre: ")
    print("Ingrese las notas:")
    for j in range(DIMNOTAS):
        pacientes[i]["consultas"][j] = int(input(":"))

print(" ")
print("     DNI   Consultas Totales ")
for i in range(DIM):
    totalConsultas = 0
    for j in range(DIMNOTAS):
        totalConsultas = totalConsultas + pacientes[i]["consultas"][j]
    print("  ",pacientes[i]["dni"],"   ",totalConsultas)


print(" ")
mayorNota = 0
aux = 0
for i in range(DIM):
    # Se considera la posición 7 como el valor que indica el mes de agosto
    if i == 0:
        mayorNota = pacientes[i]["consultas"][7]
        aux = pacientes[i]["dni"]
    else:
        if pacientes[i]["consultas"][7] > mayorNota:
            mayorNota = pacientes[i]["consultas"][7]
            aux = pacientes[i]["dni"]
print("El paciente con DNI",aux,"tuvo la mayor cantidad de consultas (",mayorNota,") en el mes de agosto")