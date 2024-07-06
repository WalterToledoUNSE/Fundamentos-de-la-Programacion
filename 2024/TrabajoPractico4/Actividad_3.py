import numpy as np
import datetime

def cargarEstático(me):
    me[0] = (123,23456789,'Juan',(12,12,1975),'M',12,(12,2,2019),1)
    me[1] = (124,44567892,'Pedro',(25,6,1956),'M',11,(23,8,1998),1)
    me[2] = (125,34567892,'Maria',(7,1,1987),'F',12,(4,6,2015),1)
    me[3] = (126, 8567892, 'Mirta', (7, 1, 1952), 'F', 11, (4, 6, 1971), 2)

    return 4

def activosfemeninos(emp,d):
    print("Nro Legajo     Nombre")
    for i in range(d):
        if emp[i]['sexo'] == 'F' and emp[i]['estado'] == 1:
            print(emp[i]['nro_legajo'], end="            ")
            print(emp[i]['nombre'], end="  ")
    return None

def diferencia(anio):
    actual = datetime.datetime.now().year
    dif = actual - anio
    return dif

def antiaguedadveinticinco(emp,d):
    print("\n")
    print("Empleados con antiguedad de 25 años")
    for i in range(d):
        ant = diferencia(emp[i]['fecha_ingreso']['anio'])
        if ant == 25:
            print(emp[i]['nro_legajo'])
    return None

def paraJubilarse(emp, d):
    print("\n")
    print("Empleados con edad para jubilarse")
    for i in range(d):
        edad = diferencia(emp[i]['fecha_nacimiento']['anio'])
        if ((edad >= 60 and emp[i]['sexo']=='F' and emp[i]['estado']!= 2)
                or
                (edad>= 65 and emp[i]['sexo']=='M' and emp[i]['estado']!= 2)):
            emp[i]['estado'] = 3
            print(emp[i]["nombre"], end="  ")
            print(edad,"Años ")
    return None

################################################
# programa principal
################################################

# Estructura de los registros
TIPO_FECHA = np.dtype(
    [
        ('dia', int),
        ('mes', int),
        ('anio', int)
    ]
)

TIPO_DOCENTE = np.dtype(
    [
        ('nro_legajo',int),
        ('dni', int),
        ('nombre','U10'),
        ('fecha_nacimiento',TIPO_FECHA),
        ('sexo', 'U1'),
        ('cod_facultad', int),
        ('fecha_ingreso',TIPO_FECHA),
        ('estado', int)
    ]
)
N = 4
empleados = np.empty(N,dtype=TIPO_DOCENTE)

dimL = cargarEstático(empleados)
activosfemeninos(empleados,dimL)
antiaguedadveinticinco(empleados,dimL)
paraJubilarse(empleados,N)