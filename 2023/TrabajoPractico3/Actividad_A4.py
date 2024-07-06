# Determinar si una fecha es válida (DD, MM, AAAA).

# Definición de Módulos
def validarFecha(dia, mes, anio):
    estado = False
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        if dia >= 1 and dia <= 31:
            estado = True
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if dia >= 1 and dia <= 30:
            estado = True
    else:
        bisiesto = esBisiesto(anio)
        if bisiesto == True:
            if dia >= 1 and dia <= 29:
                estado = True
        else:
            if dia >= 1 and dia <= 28:
                estado = True
    return estado

def esBisiesto(anio):
    estado = False
    if (anio%4 == 0 and anio%100 != 0) or (anio%400 == 0):
        estado = True
    return estado

# Programa Principal
dia = int(input("Ingrese el día (dd): "))
mes = int(input("Ingrese el mes (mm): "))
anio = int(input("Ingrese el año (aaaa): "))
resultado = validarFecha(dia,mes,anio)
if resultado:
    print("La fecha ingresada es valida")
else:
    print("La fecha ingresada no es valida")