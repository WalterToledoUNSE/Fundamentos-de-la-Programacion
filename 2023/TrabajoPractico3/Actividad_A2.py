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
numero = int(input("Ingrese un número para calcular su factorial: "))
resultado = calcularFactorial(numero)

print("El resultado es ",resultado)