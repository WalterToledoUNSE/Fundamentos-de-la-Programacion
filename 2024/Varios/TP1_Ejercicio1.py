# Un comerciante desea saber de sus N empleados:
# El mayor sueldo de 5 dígitos.
# El promedio de los sueldos entre $ 80.000 y $ 110.000 que cuyo dígito de la unidad sea igual a cero.
# El sueldo de todos sus empleados incrementados en un 15 % de su monto.

N = int(input("Ingrese la cantidad de empleados: "))
c = 0
c1 = 0
may = 0
sum = 0
while c < N:
    print("------------------------------------")
    sueldo = float(input("Ingrese el sueldo del empleado: "))

    ##########################
    #          Item 1
    ##########################
    # Se verifica que el sueldo sea de 5 digitos
    if sueldo >= 10000 and sueldo < 100000:
        # Se aplica el algoritmo de mayor
        if sueldo > may:
            may = sueldo

    ##########################
    #          Item 2
    ##########################
    # Se verifica que el sueldo este entre $80.000 y $110.000 y su unidad sea igual a cero
    if sueldo >= 80000 and sueldo <= 110000:
        # Esta operación ( % 10 ) siempre retorna el valor de la unidad
        unidad = int(sueldo % 10)  # Se usa INT para tomar la parte entera cuando se trabaje con números float
        if unidad == 0:
            sum = sum + sueldo
            c1 = c1 + 1

    ##########################
    #          Item 3
    ##########################
    # Se actualiza el sueldo actual en un 15%
    sueldoActualizado = sueldo * 1.15
    print("El sueldo actual: $%.2f" % sueldo)
    print("El sueldo actualizado es de: $%.2f"% sueldoActualizado)
    c = c + 1

print("\n")
print("El mayor sueldo sea de 5 digitos es: ",may)
print("La cantidad de empleados con sueldo entre $80.000 y $110.000 con su unidad igual a cero es de : ",c1)