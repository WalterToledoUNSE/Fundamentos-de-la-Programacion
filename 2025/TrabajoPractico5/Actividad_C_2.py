import numpy as np
import random as rd

DIM = 10
TMaterias = np.dtype([
    ('CodigoMateria', int),
    ('Nombre', 'U25'),
    ('HorasSemanales', int)
])

Materias = np.empty(DIM, dtype=TMaterias)
I = np.empty([DIM,4],dtype=int)

def cargarDatos(Materias, I, DIM):

    nulo = rd.randint(0,DIM)
    for i in range(DIM):
        codigo = rd.randint(1000,9999)
        nombre = "Materia_"+str(codigo)
        horas = rd.randint(10,65)

        Materias[i]['CodigoMateria'] = codigo
        Materias[i]['Nombre'] = nombre
        Materias[i]['HorasSemanales'] = horas

        aux = 1
        if i == nulo:
            aux = 0
        I[i][0] = codigo
        I[i][1] = rd.randint(0,50) * rd.randint(0,1) * aux
        I[i][2] = rd.randint(0,50) * aux
        I[i][3] = rd.randint(0,50) * rd.randint(0,1) * aux

def listarMaterias(Materias, DIM):
    # A. Listar_materias: Recorre todas las materias y, para cada una, llama internamente al módulo
    #    info_inscriptos. Finalmente, muestra: códigoMateria, nombre, total de inscriptos y cantidad
    #    de comisiones habilitadas de cada materia.
    print("Código Materia       Nombre            Inscriptos    Comisiones Habilitadas")
    for i in range(DIM):
        codigo = Materias[i]['CodigoMateria']
        totalInscriptos, comisionesHabilitadas, comisionMayorCantidad = infoInscriptos(I, DIM, codigo)
        print("   ", codigo, "        ",Materias[i]['Nombre'], "           ", totalInscriptos, "                 ", comisionesHabilitadas)


    return None

def infoInscriptos(I, DIM, codigo):

    totalInscriptos = 0
    comisionesHabilitadas = 0
    comisionMayorCantidad = 0
    mayor = 0

    i = 0
    bandera = False
    while i < DIM and not bandera:
        if I[i][0] == codigo:
            bandera = True
            j=1
            while j < 4:
                totalInscriptos = totalInscriptos + I[i][j]
                if I[i][j] > 0:
                    comisionesHabilitadas = comisionesHabilitadas + 1
                if j == 1:
                    comisionMayorCantidad = j
                    mayor = I[i][j]
                else:
                    if I[i][j] >= comisionMayorCantidad:
                        comisionMayorCantidad = j
                        mayor = I[i][j]
                j = j + 1
        else:
            i = i + 1
    return totalInscriptos, comisionesHabilitadas, mayor

def buscarMateriaPorCodigo(Materias, DIM, codigo):
    i = 0
    bandera = False
    pos = -1
    while i < DIM and not bandera:
        if Materias[i]['CodigoMateria'] == codigo:
            pos = i
            bandera = True
        else:
            i = i + 1
    return pos

def consulta(Materias, DIM, codigo, I):
    # B.  Consulta: Para un determinado código de materia ingresado por teclado, mostrar el nombre de
    #     la materia, la comisión con mayor cantidad de inscriptos, el total de inscriptos y la cantidad
    #     de comisiones habilitadas.

    pos = buscarMateriaPorCodigo(Materias, DIM, codigo)
    if pos >= 0:
        totalInscriptos, comisionesHabilitadas, comisionMayorCantidad = infoInscriptos(I, DIM, codigo)
        print("Materia: ",Materias[pos]['Nombre'])
        print("La comisión con mayor cantidad de inscriptos es: ", comisionMayorCantidad)
        print("El total de inscriptos es: ", totalInscriptos)
        print("La cantidad de comisiones habilitadas: ", comisionesHabilitadas)

    return None

def mostrarDatos(Materias, I, DIM):
    print("Código Materia       Nombre       Horas Semanales")
    for i in range(DIM):
        print("    ",Materias[i]['CodigoMateria'],"       ",Materias[i]['Nombre'],"         ",Materias[i]['HorasSemanales'])

    print("\n")
    print("Cód    C1    C2    C3")
    for i in range(DIM):
        for j in range(4):
            print(I[i][j], end="    ")
        print(" ")

cargarDatos(Materias,I,DIM)
mostrarDatos(Materias, I, DIM)
listarMaterias(Materias, DIM)
codigoMateria = int(input("Ingrese un código de materia: "))
consulta(Materias, DIM, codigoMateria, I)