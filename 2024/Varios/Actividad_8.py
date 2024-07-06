numero = int(input("Ingrese un número: "))
while numero != -1:
    print("La serie de Umlan es la siguiente")
    print("El número es: ", numero)
    while numero != 1:
        x = (numero // 2) * 2
        if x == numero:
            numero = int(numero / 2)
        else:
            numero = numero * 3 + 1
        print("El número es: ", numero)
    numero = int(input("Ingrese un número: "))
