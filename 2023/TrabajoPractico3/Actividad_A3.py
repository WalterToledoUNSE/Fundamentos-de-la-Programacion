# Dado los lados de un triángulo, determinar el tipo de triángulo (equilátero, isósceles, escaleno).

# Definición de Módulos
def calcularTipoTriangulo(lado1, lado2, lado3):
    tipo = ''
    if(lado1 == lado2 and lado2 == lado3):
        tipo = "Equilatero"
    else:
        if (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
            tipo = "Isósceles"
        else:
            tipo = "Escaleno"
    return tipo

# Programa Principal
l1 = float(input("Ingrese el primer lado del triangulo: "))
l2 = float(input("Ingrese el segundo lado del triangulo: "))
l3 = float(input("Ingrese el tercer lado del triangulo: "))
resultado = calcularTipoTriangulo(l1,l2,l3)

print("El resultado es:",resultado)