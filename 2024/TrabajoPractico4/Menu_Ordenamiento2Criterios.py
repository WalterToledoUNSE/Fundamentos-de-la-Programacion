import numpy as np

#Declaracion de Funciones

def cargar_pacientes(pacientes):
    pacientes[0] = (200, "Lopez Sonia", 2, 12, 1)
    pacientes[1] = (210, "Juarez Marcelo", 3, 21, 2)
    pacientes[2] = (215, "Juarez Daniel", 1, 21, 2)
    pacientes[3] = (220, "Alvarez Sonia", 2, 12, 1)
    pacientes[4] = (225, "Zanetti Pupi", 1, 21, 2)
    dim = 5
    return dim

def mostrar_menu():
    print("1.-Alta de Pacientes")
    print("2.-Informe de Obra Social")
    print("3.-Informe de Pacientes")
    print("4.-Fin")
    return None

def alta_paciente():
    print("Modulo:alta_paciente")
    return None

def  mostrar_informe_obra_social():
    print("Modulo:mostrar_informe_obra_social")
    return None

def ordenar_pacientes(pacientes, dimPac):
    aux = np.empty(1, dtype=TPaciente)
    b = True
    while b == True:
        b = False
        for i in range(0, dimPac-1):
            if pacientes[i]['codigo_osocial'] > pacientes[i+1]['codigo_osocial']:
                aux[0] = pacientes[i]
                pacientes[i]= pacientes[i+1]
                pacientes[i+1] = aux[0]
                b = True
            elif pacientes[i]['codigo_osocial'] == pacientes[i+1]['codigo_osocial']:
                if pacientes[i]['apellido_nombres'] > pacientes[i + 1]['apellido_nombres']:
                    aux[0] = pacientes[i]
                    pacientes[i] = pacientes[i + 1]
                    pacientes[i + 1] = aux[0]
                    b = True
    return None



def mostrar_informe_pacientes(pacientes, dimPac):
    ordenar_pacientes(pacientes, dimPac)
    for i in range(0,dimPac):
        print(pacientes[i]['codigo_osocial'],pacientes[i]['numero_afiliado'],pacientes[i]['apellido_nombres'])
    return None


#Programa Principal
DIM = 10
TPaciente = np.dtype(
    [('numero_afiliado',int),
     ('apellido_nombres','U50'),
     ('codigo_osocial', int),
     ('cant_dias_internacion', int),
     ('cant_dias_terapia_intensiva',int)])

pac = np.empty(DIM, dtype=TPaciente)
dimPac=cargar_pacientes(pac)

mostrar_menu()
opcion=int(input("Ingrese su opcion:"))
while opcion!=4:
    if opcion==1:
        alta_paciente()
    elif opcion==2:
        mostrar_informe_obra_social()
    elif opcion==3:
        mostrar_informe_pacientes(pac,dimPac)
    mostrar_menu()
    opcion = int(input("Ingrese su opcion:"))