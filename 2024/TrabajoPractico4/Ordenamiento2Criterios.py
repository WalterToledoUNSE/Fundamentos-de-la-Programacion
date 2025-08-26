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

def ordenar_pacientes(pacientes, dimPac):
    aux = np.empty(1, dtype=TPaciente)
    b = True
    while b == True:
        b = False
        for i in range(0, dimPac-1):
            # Primer criterio de ordenamiento
            if pacientes[i]['codigo_osocial'] > pacientes[i+1]['codigo_osocial']:
                aux[0] = pacientes[i]
                pacientes[i]= pacientes[i+1]
                pacientes[i+1] = aux[0]
                b = True
            # Si la condición del primer criterio no la cumple, verifica si es igual
            elif pacientes[i]['codigo_osocial'] == pacientes[i+1]['codigo_osocial']:
                # Se establece el segundo criterio de ordenamiento
                if pacientes[i]['apellido_nombres'] > pacientes[i + 1]['apellido_nombres']:
                    aux[0] = pacientes[i]
                    pacientes[i] = pacientes[i + 1]
                    pacientes[i + 1] = aux[0]
                    b = True
    return None
def mostrar(pacientes, dimPac):
    print('Cod OS\t\t Afiliado')
    for i in range(0, dimPac):
        print('  ', pacientes[i]['codigo_osocial'], '\t', pacientes[i]['apellido_nombres'])
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
print("El arreglo original es el siguiente...")
mostrar(pac,dimPac)
print("\nEl arreglo ordenado es el siguiente...")
ordenar_pacientes(pac,dimPac)
mostrar(pac,dimPac)
