# PACIENTES[N] los siguientes datos: DNI, ApeNom,
# Direccion (calle, nro, piso, dpto), CodigoObraSocial.

# TURNOS[M] con los siguientes datos: NroTurno, DNI, Fecha(DD, MM, AAAA),
# Especialidad, Estado (Asignado/Atendido), CodigoObraSocial.

import numpy as np

# DEFINICIÓN DE ESTRUCTURAS

TDIRECCION = np.dtype([
    ('calle','U50'),
    ('nro',int),
    ('piso',int),
    ('depto','U5'),
])

TFECHA = np.dtype([
    ('dia',int),
    ('mes',int),
    ('anio',int),
])

TPACIENTES = np.dtype([
    ('dni', int),
    ('apeNom', 'U30'),
    ('direccion', TDIRECCION),
    ('codigoOS', int),
])

TTURNOS = np.dtype([
    ('nroTurno',int),
    ('dni',int),
    ('fecha',TFECHA),
    ('especialidad','U30'),
    ('codOS',int),
    ('estado',int), # 1.Asignado   0.Atendido
])

# DEFINICIÓN DE MÓDULOS

def cargarPacientes(P):
    dim = 5
    P[0]['dni'] = 1053
    P[0]['apeNom'] = 'Coria, Agustin'
    P[0]['direccion']['calle'] = 'Belgrano'
    P[0]['direccion']['nro'] = 23
    P[0]['direccion']['piso'] = 1
    P[0]['direccion']['depto'] = 'D'
    P[0]['codigoOS'] = 1

    P[1]['dni'] = 1054
    P[1]['apeNom'] = 'Coria 1, Agustin 1'
    P[1]['direccion']['calle'] = 'Belgrano 1'
    P[1]['direccion']['nro'] = 30
    P[1]['direccion']['piso'] = 2
    P[1]['direccion']['depto'] = 'C'
    P[1]['codigoOS'] = 1

    P[2]['dni'] = 2050
    P[2]['apeNom'] = 'Coria 2, Agustin 2'
    P[2]['direccion']['calle'] = 'Belgrano 2'
    P[2]['direccion']['nro'] = 250
    P[2]['direccion']['piso'] = 0
    P[2]['direccion']['depto'] = '-'
    P[2]['codigoOS'] = 2

    P[3]['dni'] = 3152
    P[3]['apeNom'] = 'Coria 3, Agustin 3'
    P[3]['direccion']['calle'] = 'Belgrano 3'
    P[3]['direccion']['nro'] = 185
    P[3]['direccion']['piso'] = 9
    P[3]['direccion']['depto'] = 'F'
    P[3]['codigoOS'] = 2

    P[4]['dni'] = 4285
    P[4]['apeNom'] = 'Coria 4, Agustin 4'
    P[4]['direccion']['calle'] = 'Belgrano 4'
    P[4]['direccion']['nro'] = 365
    P[4]['direccion']['piso'] = 4
    P[4]['direccion']['depto'] = 'A'
    P[4]['codigoOS'] = 3

    return dim

def mostrarPacientes(P, dimP):
    for i in range(dimP):
        print("DNI: ", P[i]['dni'])
        print("Apellido y Nombre: ", P[i]['apeNom'])
        print("Dirección: ", P[i]['direccion'])
        print("Código Obra Social: ", P[i]['codigoOS'])
        print("")

    return None
def cargarTurnos(T):
    dim = 5
    T[0]['nroTurno'] = 1000
    T[0]['dni'] = 1053
    T[0]['fecha']['dia'] = 10
    T[0]['fecha']['mes'] = 10
    T[0]['fecha']['anio'] = 2025
    T[0]['especialidad'] = 'Clinica General'
    T[0]['codOS'] = 2
    T[0]['estado'] = 1

    T[1]['nroTurno'] = 1001
    T[1]['dni'] = 1054
    T[1]['fecha']['dia'] = 11
    T[1]['fecha']['mes'] = 10
    T[1]['fecha']['anio'] = 2025
    T[1]['especialidad'] = 'Cardiología'
    T[1]['codOS'] = 1
    T[1]['estado'] = 1

    T[2]['nroTurno'] = 1002
    T[2]['dni'] = 2050
    T[2]['fecha']['dia'] = 11
    T[2]['fecha']['mes'] = 10
    T[2]['fecha']['anio'] = 2025
    T[2]['especialidad'] = 'Cardiología'
    T[2]['codOS'] = 3
    T[2]['estado'] = 1

    T[3]['nroTurno'] = 1003
    T[3]['dni'] = 3152 # 4285
    T[3]['fecha']['dia'] = 12
    T[3]['fecha']['mes'] = 10
    T[3]['fecha']['anio'] = 2025
    T[3]['especialidad'] = 'Oftalmología'
    T[3]['codOS'] = 2
    T[3]['estado'] = 1

    T[4]['nroTurno'] = 1004
    T[4]['dni'] = 4285
    T[4]['fecha']['dia'] = 13
    T[4]['fecha']['mes'] = 10
    T[4]['fecha']['anio'] = 2025
    T[4]['especialidad'] = 'Oftalmología'
    T[4]['codOS'] = 3
    T[4]['estado'] = 1

    return dim
def mostrarTurnos(T, dimT):
    for i in range(dimT):
        print("Nro Turno: ", T[i]['nroTurno'])
        print("DNI: ", T[i]['dni'])
        print("Fecha: ", T[i]['fecha'])
        print("Especialidad: ", T[i]['especialidad'])
        print("Código Obra Social: ", T[i]['codOS'])
        print("Estado: ", T[i]['estado'])
        print("")

    return None
def buscarTurno(T, dimT, numeroTurno):
    existe = -1
    for i in range(dimT):
        if T[i]['nroTurno'] == numeroTurno:
            existe = i
    return existe

def eliminarTurno(T, dimT, numeroTurno):
    i = buscarTurno(T, dimT, numeroTurno)
    if i >= 0:
        print("Eliminar / Actualizar estado")
        T[i]['estado'] = 0
    else:
        print("No existe el número de turno ingresado...")
    return None
def ordenarTurnos(T, dimT):
    aux = np.empty(1,dtype=TTURNOS)
    i = 0
    while i < dimT - 1:
        p = i
        j = i + 1
        while j < dimT:
            # En este condicional el signo "< o >" determina el orden ascendente o descendente
            if T[j]['codOS'] < T[p]['codOS']:
                p = j
            j += 1
        aux[0] = T[p]
        T[p] = T[i]
        T[i] = aux[0]
        i += 1
    return None

def buscarPaciente(P, dimP, dni):
    existe = -1
    for i in range(dimP):
        if P[i]['dni'] == dni:
            existe = i
    return existe

def buscarObraSocial(codigoOS):
    nombre = ''
    if codigoOS == 1:
        nombre = 'SMAUNSE'
    else:
        if codigoOS == 2:
            nombre = 'OSDE'
        else:
            nombre = 'OSPEC'
    return nombre


def generarInforme(T, dimT, P, dimP):
    ordenarTurnos(T,dimT)
    i = 0
    print('Informe de pacientes atendidos')
    while i < dimT:
        auxCodOS = T[i]['codOS']
        nombre = buscarObraSocial(auxCodOS)
        print('Código de Obra Social: ',auxCodOS, '    Nombre:',nombre)
        print('DNI         Apellido y Nombre            Fecha')
        while i < dimT and auxCodOS == T[i]['codOS']:
            if T[i]['estado'] == 1:
                dni = T[i]['dni']
                indiceP = buscarPaciente(P, dimP, dni)
                print(T[i]['dni'],'      ',P[indiceP]['apeNom'],'      ',T[i]['fecha'])
            i = i + 1
        print(" ")

# PROGRAMA PRINCIPAL

DIM_TURNOS = 50
DIM_PACIENTES = 20

dimT = 0
dimP = 0

P = np.empty(DIM_PACIENTES, dtype=TPACIENTES)
T = np.empty(DIM_TURNOS, dtype=TTURNOS)

dimP = cargarPacientes(P)
mostrarPacientes(P,dimP)

dimT = cargarTurnos(T)
mostrarTurnos(T, dimT)

# numeroTurno = int(input('Ingrese el número de turno a eliminar: '))
# eliminarTurno(T,dimT, numeroTurno)
# print("Turnos Actualizados...")
# mostrarTurnos(T, dimT)

generarInforme(T, dimT, P, dimP)
