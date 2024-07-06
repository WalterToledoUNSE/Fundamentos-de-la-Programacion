numero = int(input("Ingrese un número: "))
valor = int(input("Ingrese un valor: "))
contCapicua = 0
contDec = 0
while numero > 0:
    decMil = numero//10000
    aux1 = numero - (decMil * 10000)
    uniMil = aux1//1000
    aux2 = aux1 - (uniMil * 1000)
    cen = aux2 // 100
    aux3 = aux2 - (cen * 100)
    dec = aux3 // 10
    uni = aux3 - (dec * 10)

    if decMil > 0:
        if uni == decMil and dec == uniMil:
            print("El número ingresado es capicua: ",numero)
            contCapicua=+1
        digIzquierda = decMil
    else:
        if uniMil > 0:
            if uni == uniMil and dec == cen:
                print("El número ingresado es capicua: ", numero)
                contCapicua = +1
            digIzquierda = uniMil
        else:
            if cen > 0:
                if uni == cen:
                    print("El número ingresado es capicua: ", numero)
                    contCapicua = +1
                digIzquierda = cen
            else:
                if dec > 0:
                    if uni == dec:
                        print("El número ingresado es capicua: ", numero)
                        contCapicua = +1
                    digIzquierda = dec
                else:
                    digIzquierda = uni
    if dec < valor:
        contDec =+ 1
    if digIzquierda > 4:
        imp = numero % 2
        if imp != 0:
            print("El digito de la izquierda es mayor a 4 e impar: ",numero)
    numero = int(input("Ingrese un número: "))
print("La cantidad de números capicúas ingresados es: ",contCapicua)
print("La cantidad de números con decena menor a ",valor," es de: ",contDec)