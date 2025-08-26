import numpy as np

def cargar_alumnos_estatico(v):
    v[0] = (39876543,'Perez Juan', 123, 1)
    v[1] = (29856543, 'Gomez María', 345, 2)
    v[2] = (27877543, 'Sanchez Silvia', 246, 2)
    v[3] = (49835632, 'Gonzalez Lionel', 578, 1)
    return 4

def buscar_alumno(v,d, dni):
    b = False
    for i in range(d):
        if v[i]['dni'] == dni:
            b = True
    return b

def cargar_alumnos_dinamico(v,d, DIM):
    dni = int(input("Ingrese el nro de DNI (0 para Salir): "))
    while dni != 0 and d < DIM:
        if not(buscar_alumno(v,d,dni)):
            v[d]['dni'] = dni
            v[d]['apeNom'] = input("Ingrese el nombre del alumno: ")
            v[d]['nroLegajo'] = int(input("Ingrese el nro de legajo: "))
            d += 1
        else:
            print("Alumno existente")
        print("----")
        dni = int(input("Ingrese el nro de DNI (0 para Salir): "))
    return d

def mostrar_vector(v,d):
    print("DNI         Apellido y Nombre    Nro de Legajo     Tipo")
    for i in range(d):
        print(v[i]['dni'], end="    ")
        print("{:25}".format(v[i]['apeNom']), end=" ")
        print(v[i]['nroLegajo'], end= "            ")
        print(v[i]['tipo'])


def ordenar_vector(vector, d):
    aux = np.empty(1,dtype=alumno)
    i = 0
    while i < d:
        p = i
        j = i + 1
        while j < d:
            if vector[j]['apeNom'] < vector[p]['apeNom']:
                p = j
            j += 1
        aux[0] = vector[p]
        vector[p] = vector[i]
        vector[i] = aux[0]
        i += 1


def ordenar_vector_dos_criterios(vector, d):
    aux = np.empty(1,dtype=alumno)
    i = 0
    while i < d:
        p = i
        j = i + 1
        while j < d:
            if (vector[j]['tipo'] < vector[p]['tipo']) or \
                    (vector[j]['tipo'] == vector[p]['tipo'] and
                     vector[j]['apeNom'] < vector[p]['apeNom']):
                p = j
            j += 1
        aux[0] = vector[p]
        vector[p] = vector[i]
        vector[i] = aux[0]
        i += 1

# Programa principal

alumno = np.dtype([
    ('dni',int),
    ('apeNom','U20'),
    ('nroLegajo', int),
    ('tipo', int)
])

DIM = 100
vector_alumnos = np.empty(DIM, dtype=alumno)

dim = cargar_alumnos_estatico(vector_alumnos)
#dim = cargar_alumnos_dinamico(vector_alumnos,dim,DIM)
mostrar_vector(vector_alumnos,dim)
ordenar_vector(vector_alumnos,dim)
print("Vector ordenado por nombre")
mostrar_vector(vector_alumnos,dim)
print("Vector ordenado por tipo y nombre")
ordenar_vector_dos_criterios(vector_alumnos,dim)
mostrar_vector(vector_alumnos,dim)