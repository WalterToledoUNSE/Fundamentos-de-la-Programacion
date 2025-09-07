# 3. Un torneo de videojuegos registra a cada jugador en un arreglo tipo registro
#    JUGADORES[K] con: CodigoJugador (entero),  Equipo { NombreEquipo, País}, PuntajeTotal (entero)
#    Se pide elaborar un diagrama de flujo que permita:
#       a) Mostrar el CodigoJugador y el País de todos los jugadores que superen los 1000 puntos.
#       b) Ordenar ascendentemente el vector por NombreEquipo.

import numpy as np
import random as rd

# Definición de las estructuras
TEquipo = np.dtype([
    ('nombreEquipo','U25'),
    ('pais','U25')
])

TJugadores = np.dtype([
    ('codigoJugador',int),
    ('equipo',TEquipo),
    ('puntajeTotal',int)
])

K = 10

jugadores = np.empty(K,dtype=TJugadores) # Se genera el arreglo de tipo TJugadores
aux = np.empty(1,dtype=TJugadores) # Se genera un registro de tipo TJugadores

for i in range(K):
    # Carga aleatoria de datos:
    jugadores[i]["codigoJugador"] = rd.randint(1000, 9999) # Se genera un número entero aleatorio entre 100 y 999
    jugadores[i]["equipo"]["nombreEquipo"] = rd.choice(["Boca        ", "River       ","Racing      ","Independiente"]) # Se obtiene un pais aleatorio desde el arreglo
    jugadores[i]["equipo"]["pais"] = rd.choice(["Argentina", "Colombia ","Brasil   ","Ecuador  "]) # Se obtiene un pais aleatorio desde el arreglo
    jugadores[i]["puntajeTotal"] = rd.randint(100, 5000)# Se genera un valor aleatorio entre 10 y 99

# Se muestra los resultados del arreglo
print("************************************************************")
print("*                   Listado de Jugadores                   *")
print("************************************************************")
print("#  Código \t\tEquipo\t\t\tPais\t   Puntaje") # El simbolo \t es una tabulación
for i in range(K):
    print((i+1),".",jugadores[i]["codigoJugador"],"\t",jugadores[i]["equipo"]["nombreEquipo"],"\t ",jugadores[i]["equipo"]["pais"], "\t",jugadores[i]["puntajeTotal"])

# Item A
print(" ")
print("Cód Jugador \tPaís")
for i in range(K):
    if jugadores[i]["puntajeTotal"] > 1000:
        print("  ",jugadores[i]["codigoJugador"], "\t  ", jugadores[i]["equipo"]["pais"])
    i = i + 1

# Item B
i = 0
while i < K-1:
    p = i
    j = i + 1
    while j < K:
        # En este condicional el signo "< o >" determina el orden ascendente o descendente
        if jugadores[j]["equipo"]["nombreEquipo"] > jugadores[p]["equipo"]["nombreEquipo"]:
            p = j
        j = j + 1
    aux[0] = jugadores[p]
    jugadores[p] = jugadores[i]
    jugadores[i] = aux[0]
    i += 1

print("************************************************************")
print("*    Listado de Jugadores Ordenada por Nombre de Equipo    *")
print("************************************************************")
print("#  Código \t\tEquipo\t\t\tPais\t   Puntaje") # El simbolo \t es una tabulación
for i in range(K):
    print((i+1),".",jugadores[i]["codigoJugador"],"\t",jugadores[i]["equipo"]["nombreEquipo"],"\t ",jugadores[i]["equipo"]["pais"], "\t",jugadores[i]["puntajeTotal"])
