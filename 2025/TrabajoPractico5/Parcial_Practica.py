import numpy as np

TFECHA = np.dtype([
    ('dia', int),
    ('mes', int),
    ('anio', int),
])

TCHOFERES = np.dtype([
    ('IDChofer', int),
    ('Apellido', 'U25'),
    ('Nombre', 'U25')
])

TVIAJES = np.dtype([
    ('CodViaje', int),
    ('Destino','U25'),
    ('IDChofer', int),
    ('PrecioPorAsiento', float),
    ('CantTotalAsientos', int),
    ('CantAsientosVendidos', int),
    ('FechaViaje', TFECHA),
])

def cargarChoferes(C):
    C[0]['IDChofer'] = 1
    C[0]['Apellido'] = 'Gomez'
    C[0]['Nombre'] = 'Juan'

    C[1]['IDChofer'] = 2
    C[1]['Apellido'] = 'Perez'
    C[1]['Nombre'] = 'Raul'

    C[2]['IDChofer'] = 3
    C[2]['Apellido'] = 'Ruiz'
    C[2]['Nombre'] = 'Carlos'

    dim = 3

    return dim

def cargarViajes(V):
    V[0]['CodViaje'] = 4
    V[0]['Destino'] = 'Córdoba'
    V[0]['IDChofer'] = 1
    V[0]['PrecioPorAsiento'] = 40.50
    V[0]['CantTotalAsientos'] = 50
    V[0]['CantAsientosVendidos'] = 30
    V[0]['FechaViaje']['dia'] = 1
    V[0]['FechaViaje']['mes'] = 10
    V[0]['FechaViaje']['anio'] = 2025

    V[1]['CodViaje'] = 2
    V[1]['Destino'] = 'Tucumán'
    V[1]['IDChofer'] = 2
    V[1]['PrecioPorAsiento'] = 18.50
    V[1]['CantTotalAsientos'] = 50
    V[1]['CantAsientosVendidos'] = 40
    V[1]['FechaViaje']['dia'] = 3
    V[1]['FechaViaje']['mes'] = 10
    V[1]['FechaViaje']['anio'] = 2025

    V[2]['CodViaje'] = 3
    V[2]['Destino'] = 'Bs As'
    V[2]['IDChofer'] = 3
    V[2]['PrecioPorAsiento'] = 125
    V[2]['CantTotalAsientos'] = 60
    V[2]['CantAsientosVendidos'] = 42
    V[2]['FechaViaje']['dia'] = 5
    V[2]['FechaViaje']['mes'] = 10
    V[2]['FechaViaje']['anio'] = 2025

    V[3]['CodViaje'] = 1
    V[3]['Destino'] = 'Salta'
    V[3]['IDChofer'] = 1
    V[3]['PrecioPorAsiento'] = 68.50
    V[3]['CantTotalAsientos'] = 55
    V[3]['CantAsientosVendidos'] = 38
    V[3]['FechaViaje']['dia'] = 10
    V[3]['FechaViaje']['mes'] = 11
    V[3]['FechaViaje']['anio'] = 2025

    dim = 4
    return dim

def buscarChofer(idChofer, C, dimC):
    pos = -1
    for i in range(dimC):
        if C[i]['IDChofer'] == idChofer:
            pos = i
    return pos

def buscarViaje(codViaje, V, dimV):
    pos = -1
    for i in range(dimV):
        if V[i]['CodViaje'] == codViaje:
            pos = i
    return pos

def consultaDeUnViaje(codViaje, V, dimV, C, dimC):
    i = buscarViaje(codViaje, V, dimV)
    if i >= 0:
        idChofer = V[i]['IDChofer']
        j = buscarChofer(idChofer, C, dimC)
        importeTotal = V[i]['PrecioPorAsiento'] * V[i]['CantAsientosVendidos']
        fechaF = formatoFecha(V[i]['FechaViaje'])
        print('MovilBus - Informe de Viajes')
        print('Código de Viaje: ', codViaje, '        Apellido y Nombre:', C[j]['Apellido'],', ',C[j]['Nombre'])
        print('Destino: ', V[i]['Destino'], '         Cantidad de Asientos Vendidos:',V[i]['CantAsientosVendidos'])
        print('Importe: ', V[i]['PrecioPorAsiento'],'      Importe Total: ',importeTotal, '        Fecha:',fechaF)
    else:
        print('Viaje Inexistente')
    return None

def registrarVentasDePasajes(codViaje, cantidadAVender, V, dimV):
    i = buscarViaje(codViaje,V, dimV)
    if i >= 0:
        if cantidadAVender > 0:
            capacidad = V[i]['CantAsientosVendidos'] + cantidadAVender
            if capacidad <= V[i]['CantTotalAsientos']:
                print('Venta Realizada...')
                V[i]['CantAsientosVendidos'] = V[i]['CantAsientosVendidos'] + cantidadAVender
                disponible = V[i]['CantTotalAsientos'] - V[i]['CantAsientosVendidos']
                print('La cantidad de asientos disponibles es de: ',disponible)
                print('')
            else:
                print('Asientos Insuficientes')
        else:
            print('Cantidad Inválida')
    else:
        print('No existe el viaje')
    return None

def formatoFecha(fecha):
    return str(fecha['dia'])+'/'+str(fecha['mes'])+'/'+str(fecha['anio'])
def listadoDeViajes(mes, V, dimV, C, dimC):
    cantidadViajes = contarViajes(mes, V, dimV)
    ordenarViajes(V,dimV)
    print('Listado de Viaje Mes: ',cantidadViajes)
    print('Codigo Viaje \t Chofer \t\t Destino \t\t Pasajeros \t Fecha')
    for i in range(dimV):
        if V[i]['FechaViaje']['mes'] == mes:
            idChofer = V[i]['IDChofer']
            pos = buscarChofer(idChofer, C, dimC)
            chofer = C[pos]['Apellido']+','+C[pos]['Nombre']
            fechaF = formatoFecha(V[i]['FechaViaje'])

            print(V[i]['CodViaje'],'\t\t',chofer,'\t\t',V[i]['Destino'],'\t\t',V[i]['CantAsientosVendidos'],'\t\t',fechaF)
    return None
def contarViajes(mes, V, dimV):
    cantidad = 0
    for i in range(dimV):
        if V[i]['FechaViaje']['mes'] == mes:
            cantidad = cantidad + 1
    return cantidad

def ordenarViajes(V, dimV):
    i = 0
    aux = np.empty(1,dtype=TVIAJES)
    while i < dimV - 1:
        p = i
        j = i + 1
        while j < dimV:
            # En este condicional el signo "< o >" determina el orden ascendente o descendente
            if V[j]['CodViaje'] < V[p]['CodViaje']:
                p = j
            j += 1
        aux[0] = V[p]
        V[p] = V[i]
        V[i] = aux[0]
        i += 1

# Programa Principal

DIMV = 50
DIMC = 20
V = np.empty(DIMV, dtype=TVIAJES)
C = np.empty(DIMC, dtype=TCHOFERES)

dimC = cargarChoferes(C)
dimV = cargarViajes(V)

codViaje = int(input('Ingrese el código del viaje:'))
consultaDeUnViaje(codViaje, V, dimV, C, dimC)

print(' ')
codigoViaje = int(input('Ingrese el código del viaje:'))
cantAVender = int(input('Ingrese la cantidad de asientos:'))
registrarVentasDePasajes(codigoViaje,cantAVender,V,dimV)

print(' ')
mes = 0
while mes < 1 or mes > 12:
    mes = int(input('Ingrese el mes:'))
listadoDeViajes(mes, V, dimV, C, dimC)