# Para una serie de números enteros (pueden ingresar números de 1 dígito
# hasta 5 dígitos), cuyo final viene dado por el ingreso del número 0, se pide:
# a) Calcular y mostrar los números que son Capicúas.
# b) Mostrar la cantidad de números cuyo dígito de la decena sea menor a un determinado valor.
# c) Mostrar todos los números cuyo primer dígito de la izquierda sea impar mayor a 4.

numero = -1; cantidadCapicuas = 0; cantidadValorDeterminado = 0; digitoIzquierda = 0
valorDeterminado = int(input("Ingrese un número determinado: "))
while numero != 0:
    numero = int(input("Ingrese un número (0 al 99.999): "))

    # Se realiza ciclo para garantizar que el numero tenga entre 1 a 5 digitos
    while numero < 0 or numero > 99999:
        print("El número debe estar comprendido entre 0 y 99.0000")
        numero = int(input("Ingrese un número: "))

    # Si el "numero" es igual a cero, no se realiza nada
    if numero != 0:
        # Se comienza a descomponer el número
        unidad = (numero // 1) % 10
        decena = (numero // 10) % 10
        centena = (numero // 100) % 10
        unidad_mil = (numero // 1000) % 10
        decena_mil = (numero // 10000) % 10
        # Punto a
        if decena_mil > 0: # Caso para número de 5 dígitos
            if decena_mil == unidad and unidad_mil == decena:
                print("El número es capicua ", numero)
                cantidadCapicuas = cantidadCapicuas + 1
            digitoIzquierda = decena_mil # Punto c
        else:
            if unidad_mil > 0: # Caso para número de 4 dígitos
                if unidad_mil == unidad and centena == decena:
                    print("El número es capicua ", numero)
                    cantidadCapicuas = cantidadCapicuas + 1
                digitoIzquierda = unidad_mil # Punto c
            else:
                if centena > 0: # Caso para número de 3 dígitos
                    if centena == unidad:
                        print("El número es capicua ", numero)
                        cantidadCapicuas = cantidadCapicuas + 1
                    digitoIzquierda = centena # Punto c
                else:
                    if decena > 0: # Caso para número de 2 dígitos
                        if decena == unidad:
                            print("El número es capicua ", numero)
                            cantidadCapicuas = cantidadCapicuas + 1
                        digitoIzquierda = decena # Punto c
                    else:
                        digitoIzquierda = unidad # Punto c
        # Punto b
        if numero > 9:
            if decena < valorDeterminado:
                cantidadValorDeterminado = cantidadValorDeterminado + 1
        # Punto c
        auxEsParImpar = digitoIzquierda % 2
        if auxEsParImpar != 0 and digitoIzquierda > 4:
            print("El número tiene su primer dígito de la izquierda impar mayor a 4:")
print("\n------------------------------------------------")
print("La cantidad de números capicuas es de :",cantidadCapicuas)
print("------------------------------------------------")
print("La cantidad de números cuyo dígito de la decena")
print("sea menor a un determinado valor es de:",cantidadValorDeterminado)
print("------------------------------------------------")