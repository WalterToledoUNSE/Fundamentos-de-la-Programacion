# Para N números, indicar cuantos son de tres dígitos y múltiplos de 4.

# Definición de Módulos
def validarNumero(numero):
    estado = False
    if numero >= 100 and numero <= 999:
        if numero % 4 == 0:
            estado = True
    return estado

# Programa Principal
cant = 0
N = 0
valido = False
while not valido:
    N = int(input("Ingrese el valor de N: "))
    if N > 0:
        valido = True
    else:
        print("El valor de N, no puede ser menor o igual a cero.")

for i in range(N):
    num = int(input("Ingrese un número:"))
    esValido = validarNumero(num)
    if esValido:
        cant+=1

print("La cantidad número de tres dígitos y múltiplos de cuatro es de:",cant)