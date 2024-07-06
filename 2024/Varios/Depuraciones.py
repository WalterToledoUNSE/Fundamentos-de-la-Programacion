CNUM = 3
cv = 0
# a = -2
may = 0
while cv < CNUM:
    num = int(input("Ingrese un nro: "))
    if num > may:
        may = num
    # cv += (a * 4) + 1
    cv += 1
print("El mayor es", may)