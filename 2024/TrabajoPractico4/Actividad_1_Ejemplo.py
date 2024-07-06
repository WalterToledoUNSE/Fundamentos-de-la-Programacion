import numpy as np

def cargarDinámico(me,d):
    for i in range(d):
        me[i]['dni'] = int(input("Ingrese el dni: "))
        me[i]['nombre'] = input("Ingrese el nombre: ")
        me[i]['edad'] = int(input("Ingrese la edad: "))
        me[i]['sexo'] = int(input("Ingrese el sexo (M - F): "))
    return None

def mayorMasculino(me,d):
    may = 0
    nombre = ""
    for i in range(d):
        if me[i]['sexo'] == 'M' and me[i]['edad']>may:
            may = me[i]['edad']
            nombre = me[i]['nombre']
    return nombre , may

def cargarEstático(me):
    me[0] = (23456789,'Juan',45,'M')
    me[1] = (44567892,'Pedro',58,'M')
    me[2] = (34567892,'Maria', 34,'F')

#Programa principal
# Estructura del registro
datos_persona = np.dtype(
    [
        ('dni',int),
        ('nombre','U10'),
        ('edad',int),
        ('sexo', 'U1')
    ]
)
N = 3
mis_empleados = np.empty(N,dtype=datos_persona)

cargarEstático(mis_empleados)
nom, edad = mayorMasculino(mis_empleados,N)
print("El mayor masculino es",nom,"con",edad,"años")