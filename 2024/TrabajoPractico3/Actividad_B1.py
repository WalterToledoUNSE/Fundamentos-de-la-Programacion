# A partir de 3 números muestre el mayor y el menor

# Definición de Módulos
def mostrarMayorMenor(num1,num2,num3):
    may = 1e-100 # Representa un número muy pequeño expresado en notación científica
    men = 1e100 # Representa un número muy grande expresado en notación científica

    if num1 > may:
        may = num1
    if num2 > may:
        may = num2
    if num3 > may:
        may = num3

    if num1 < men:
        men = num1
    if num2 < men:
        men = num2
    if num3 < men:
        men = num3
    print("El mayor número es ", may)
    print("El menor número es ", men)

    return None

# Programa Principal
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
mostrarMayorMenor(numero1, numero2, numero3)