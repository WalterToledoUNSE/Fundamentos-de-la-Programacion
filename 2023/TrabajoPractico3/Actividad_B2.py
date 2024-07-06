# A partir de 3 números muestre el mayor y el menor

# Definición de Módulos
def mostrarMayorMenor(num1,num2,num3):
    may = 1e-100
    men = 1e100
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

    return may, men

# Programa Principal
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
mayor, menor = mostrarMayorMenor(numero1, numero2, numero3)

print("El mayor número es ",mayor)
print("El menor número es ",menor)