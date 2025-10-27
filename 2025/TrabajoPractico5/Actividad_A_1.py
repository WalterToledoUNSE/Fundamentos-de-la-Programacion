# 1.	Definir un registro Fecha con los campos: día, mes, año. Crear una función que reciba una
# variable de tipo Fecha (DD,MM,AAAA) y retorne un valor booleano (Verdadero si la fecha es válida,
# Falso en caso contrario)
################################################
##          IMPORTACION DE LIBRERIAS          ##
################################################
import numpy as np

################################################
##          DEFINICIÓN DE ESTRUCTURAS         ##
################################################
TFecha = np.dtype([
    ('dia',int),
    ('mes',int),
    ('anio', int)
])
fecha = np.empty(1,dtype=TFecha)

################################################
##            DEFINICIÓN DE MÓDULOS           ##
################################################
def validarFecha(miFecha):
    estado = False
    if miFecha['anio'] > 0:
        if miFecha['mes'] >= 1 and miFecha['mes'] <= 12:
            # Se analiza el mes de febrero considerando el caso si es año bisiesto
            if miFecha['mes'] == 2:
                # Un año es bisiesto si cumple alguna de las siguientes condiciones:
                # Condición 1: es divisible por 4 y no es divisible por 100
                # Condición 2: es divisible por 400

                # Verifico si el año es bisiesto
                if ((miFecha['anio'] % 4 == 0 and miFecha['anio'] % 100 != 0) or (miFecha['anio'] % 400 == 0)):
                    if miFecha['dia'] >= 1 and miFecha['dia'] <= 29:
                        estado = True
                else:
                    if miFecha['dia'] >= 1 and miFecha['dia'] <= 28:
                        estado = True
            else:
                # Analizo los meses que tiene 31 dias (Enero, Marzo, Mayo, Julio, Agosto, Octubre y Diciembre)
                if miFecha['mes'] == 1 or miFecha['mes'] == 3 or miFecha['mes'] == 5 or miFecha['mes'] == 7 or miFecha['mes'] == 8 or miFecha['mes'] == 10 or miFecha['mes'] == 12:
                    if miFecha['dia'] >= 1 and miFecha['dia'] <= 31:
                        estado = True
                else:
                    # Se verifica la cantidad de dias de los meses que tienen 30 dias (Abril, Junio, Septiembre y Noviembre)
                    if miFecha['dia'] >= 1 and miFecha['dia'] <= 30:
                        estado = True
    return estado


################################################
##              PROGRAMA PRINCIPAL            ##
################################################
fecha['dia'] = int(input("Ingrese el día: "))
fecha['mes'] = int(input("Ingrese el mes: "))
fecha['anio'] = int(input("Ingrese el año: "))

estado = validarFecha(fecha) # Se llama a la funciónn validarFecha(....)
if estado:
    print("La fecha ingresada es válida")
else:
    print("La fecha ingresada no es válida")