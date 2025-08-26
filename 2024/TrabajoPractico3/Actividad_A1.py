# Calcular el área de un círculo conociendo su perímetro r = p / 2π y a = π. r2
import math as mt

def calcularArea(perimetro):

    radio = perimetro / (2 * mt.pi)
    area = mt.pi * (radio * radio)

    return area

# Programa Principal
perimetro = float(input("Ingrese el perímetro para calcular el área: "))
resultado = calcularArea(perimetro)

print("El área es ",resultado)