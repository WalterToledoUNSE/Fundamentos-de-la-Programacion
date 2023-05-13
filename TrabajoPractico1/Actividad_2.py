# 2) Un comerciante desea saber de sus N empleados:
# a) El mayor sueldo de 5 dígitos.
# b) El promedio de los sueldos entre $ 80.000 y $ 110.000 que cuyo dígito
# de la unidad sea igual a cero.
# c) El sueldo de todos sus empleados incrementados en un 15 % de su monto.

N = int(input("Ingrese la cantidad de empleados: "))
# Se pueden inicializar más de una variable en una sola línea. Para esto, se debe separar con ";"
c = 0 ; c1= 0; mayor = 0; sum = 0; prom = 0
while c < N:
    sueldo = float(input("Ingrese el sueldo del empleado: $"))
    print("El sueldo es: $",sueldo)
    # Punto "a"
    if sueldo >= 10000 and sueldo <= 99999:
        if sueldo > mayor:
            mayor = sueldo
    # Punto "b"
    if sueldo >= 80000 and sueldo <= 110000:
        unidad = sueldo % 10
        if unidad == 0:
            c1 = c1 + 1
            sum = sum + sueldo
    # Punto "c"
    sueldoActualizado = sueldo * 1.15
    # print("El sueldo incrementado es: ",sueldoActualizado) #Impreme el sueldo con el formato estandar de más de 2 decimales
    print("El sueldo incrementado es: $ %.2f"%sueldoActualizado) #Imprime el sueldo solamente con 2 decimales.
    c = c + 1
print(" \n----------------------------------------------------------------------")
print("El mayor sueldo de 5 dígitos es: $",mayor)
if c1 > 0: # Esta condición evita la división por cero
    prom = sum / c1
print("----------------------------------------------------------------------")
print("El promedio de los sueldos entre $ 80.000 y $ 110.000 que cuyo dígito")
print("de la unidad sea igual a cero es de $",prom)
print("----------------------------------------------------------------------")