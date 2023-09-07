# Dado un número X de 3 cifras determine la cantidad de dígitos pares y
# la cantidad de dígitos impares. Ejemplo: Si el número de tres cifras es 364,
# la cantidad de pares es 2 y la cantidad de impares es 1.

# Definición de Módulos
def determinarParesImpares(numX):
    par = 0
    impar = 0

    centena = numeroX // 100
    decena = (numeroX % 100)//10
    unidad = numeroX % 10

    if centena % 2 > 0:
        impar = impar + 1
    else:
        par = par + 1

    if decena % 2 > 0:
        impar = impar + 1
    else:
        par = par + 1

    if unidad % 2 > 0:
        impar = impar + 1
    else:
        par = par + 1

    return par, impar

# Programa Principal
numeroX = int(input("Ingrese el primer número: "))
digitoPar, digitoImpar = determinarParesImpares(numeroX)

print("La cantidad de dígitos pares es ",digitoPar)
print("La cantidad de dígitos impares es ",digitoImpar)