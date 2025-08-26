# Dado un número X de 3 cifras determine la cantidad de dígitos pares y
# la cantidad de dígitos impares. Ejemplo: Si el número de tres cifras es 364,
# la cantidad de pares es 2 y la cantidad de impares es 1.

# Definición de Módulos
def determinarParesImpares(numX):
    par = 0
    impar = 0

    centena = numX // 100 # Se realiza la division entera
    decena = (numX % 100)//10 # Realiza el módulo 100 para obtener un número de 2 cifras y luego toma la parte entera.
    unidad = numX % 10 # El módulo 10, siempre retorna el valor de la unidad

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
valido = False
# Se genera un ciclo para garantizar que los lados del triangulo sean positivos.
while not valido:
    numeroX = int(input("Ingrese el número X: "))
    numeroX = abs(numeroX)
    if numeroX >= 100 and numeroX <= 999:
        valido = True
    else:
        print("El número ingresado no tiene 3 digitos.")


digitoPar, digitoImpar = determinarParesImpares(numeroX)

print("La cantidad de dígitos pares es ",digitoPar)
print("La cantidad de dígitos impares es ",digitoImpar)