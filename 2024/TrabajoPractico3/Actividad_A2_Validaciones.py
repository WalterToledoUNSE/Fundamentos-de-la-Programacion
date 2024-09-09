# Calcular el factorial de un número. (El factorial de un número entero positivo se define como el
# producto de todos los números naturales anteriores o iguales a él).

# Definición de Módulos
def calcularFactorial(numero):
    factorial = 1
    i = numero
    while i > 1:
        factorial = factorial * i
        i = i - 1
    return factorial

# Programa Principal
numero = 0
valido = False
# Se genera un ciclo para garantizar que el número no sea negativo
while not valido:
    numero = int(input("Ingrese un número para calcular su factorial: "))
    if numero >= 0:
        valido = True
    else:
        print("El número no puede ser negativo")
resultado = calcularFactorial(numero)
print("El resultado es ",resultado)