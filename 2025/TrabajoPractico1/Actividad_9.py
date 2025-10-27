numero = int(input("Ingrese un numero: "))
while(numero != -1):
    print(numero)
    while(numero != 1):
        if numero % 2 == 0:
            numero = int (numero / 2)
        else:
            numero = numero * 3 + 1
        print(numero)
    numero = int(input("Ingrese un numero: "))