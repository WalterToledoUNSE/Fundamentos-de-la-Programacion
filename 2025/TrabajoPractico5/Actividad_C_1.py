# Un estacionamiento registra para cada uno de sus 50 lugares en un arreglo
# de tipo registro PLAYA la siguiente información: Número de Lugar (entero),
# Tipo de Vehículo (auto, moto, camioneta, utilitario), Tarifa por Hora (real),
# Estado Actual de la Plaza (ocupada, libre), Cantidad de Horas Ocupadas (entero)
# Se pide calcular e imprimir:
# A. La recaudación de un determinado lugar, teniendo en cuenta la cantidad
#     de horas ocupadas.
# B. El porcentaje de ocupación actual del estacionamiento, y el porcentaje
# de ocupación de cada uno de los cuatro tipos de vehículos registrados.

import numpy as np

DIM_FISICA = 50

TPLAYA = np.dtype([
    ("NumeroLugar", int),
    ("TipoVehiculo", int), # 1. auto, 2. moto, 3. camioneta, 4. utilitario
    ("TarifaHora", float),
    ("EstadoActual", int), # 1. ocupada, 0. libre
    ("CantidadHorasOcupadas", int)
])

def buscarLugar(playa, dimL, lugar):
    posicion = -1
    band = False
    i = 0
    while i < dimL and not band:
        if playa[i]["NumeroLugar"] == lugar:
            band = True
            posicion = i
        i = i + 1

    return posicion

def calcularOcupacion(playa, dimL):
    porcentajeTotal = 0
    porcentajeAuto = 0
    porcentajeMoto = 0
    porcentajeCamioneta = 0
    porcentajeUtilitario = 0

    return porcentajeTotal, porcentajeAuto, porcentajeMoto, porcentajeCamioneta, porcentajeUtilitario

def mostrarDatos(playa,dimL):
    print("El valor de la dimension es:  ", dimL)
    print("\nLos datos del Estacionamiento son los siguientes:")
    for i in range(dimL):
        if playa[i]["EstadoActual"] == 1:
            estado = "Ocupado"
        else:
            estado = "Libre"

        if playa[i]["TipoVehiculo"] == 1:
            tipo = "Auto"
        else:
            if playa[i]["TipoVehiculo"] == 2:
                tipo = "Moto"
            else:
                if playa[i]["TipoVehiculo"] == 3:
                    tipo = "Camioneta"
                else:
                    tipo = "Utilitario"

        print("Lugar: ",playa[i]["NumeroLugar"])
        print("Tipo Vehiculo: ",tipo)
        print("Tarifa: $ %.2f"%playa[i]["TarifaHora"])
        print("Horas Ocupadas: ",playa[i]["CantidadHorasOcupadas"])
        print("Estado: ",estado)
        print("\n")

    return None

def cargarDatos(playa):
    dimL = 0
    n = 2
    for i in range(n):
        print("Ingrese los siguientes datos: ")
        playa[i]["NumeroLugar"] = int(input("Número de Lugar: "))
        playa[i]["TipoVehiculo"] = int(input("Tipo de Vehiculo (1. auto, 2. moto, 3. camioneta, 4. utilitario): "))
        playa[i]["TarifaHora"] = float(input("Tarifa: "))
        playa[i]["CantidadHorasOcupadas"] = int(input("Cantidad de Horas: "))
        playa[i]["EstadoActual"] = 1
        dimL = dimL + 1

    return dimL

# Programa Principal
playa = np.empty(DIM_FISICA, dtype=TPLAYA)
dimL = cargarDatos(playa)
mostrarDatos(playa, dimL)
lugar = int(input("Ingresar el número de lugar: "))
pos = buscarLugar(playa, dimL, lugar)
if pos >= 0:
    recaudacion = playa[pos]["TarifaHora"] * playa[pos]["CantidadHorasOcupadas"]
    print("La recaudación es: ",recaudacion)
else:
    print("No existe el número de lugar ingresado")