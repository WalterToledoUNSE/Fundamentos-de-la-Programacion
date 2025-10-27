N = int(input("Ingrese el valor de N:"))
c = 0
muj20dias = 0
cmuj = 0
cvar = 0
diasTrabM = 0
diasTrabV = 0
while c < N:
    dni = int(input("Ingrese el DNI:"))
    sexo = int(input("Ingrese el sexo (1.Varon, 2.Mujer):"))
    diasT = int(input("Ingrese los dias trabajados:"))
    print("\n")
    if sexo == 1:
        if diasT < 20:
            muj20dias = muj20dias + 1
        cmuj = cmuj + 1
        diasTrabM = diasTrabM + diasT
    else:
        cvar = cvar + 1
        diasTrabV = diasTrabV + diasT
    c = c + 1
print("La cantidad de mujeres que trabajaron menos de 20 días es de: ",muj20dias)
if cvar > 0:
    promV = (9000 * diasTrabV) /cvar
    print("El promedio de sueldo de los empleados varones es de: ", promV)