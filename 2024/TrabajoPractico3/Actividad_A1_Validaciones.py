# Calcular el área de un círculo conociendo su perímetro r = p / 2π y a = π. r2
import math as mt

def calcularArea(perimetro):
    radio = perimetro / (2 * mt.pi)
    area = mt.pi * (radio * radio)

    return area

# Programa Principal
perimetro = 0
valido = False
# Se genera un ciclo para garantizar que el perímetro sea mayor a cero
while not valido:
    perimetro = float(input("Ingrese el perímetro para calcular el área: "))
    if perimetro > 0:
        valido = True
    else:
        print("El perímetro debe ser mayor a cero.")
resultado = calcularArea(perimetro)

print("El área es ",resultado)