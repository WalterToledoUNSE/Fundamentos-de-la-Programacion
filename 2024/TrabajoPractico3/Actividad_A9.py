# Para una serie de ternas de números, cuyo final viene dado por el valor cero, indicar el mayor de cada terna.

# Definición de Módulos
def calcularMayor(pri,seg,ter):
    mayor = 0
    if pri >= seg and pri >= ter:
        mayor = pri
    elif seg >= ter and seg >= pri:
        mayor = seg
    else:
        mayor = ter
    return mayor

# Programa Principal

bandera = False
while not bandera:
    primer = int(input("Ingrese el primer número:"))
    segundo = int(input("Ingrese el segundo número:"))
    tercer = int(input("Ingrese el tercer número:"))

    if primer == 0 and segundo == 0 and tercer == 0:
        bandera = True
    else:
        mayor = calcularMayor(primer, segundo, tercer)
        print("El mayor número de la terna es", mayor)
