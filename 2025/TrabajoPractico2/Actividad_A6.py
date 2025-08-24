# Actividad 6
# Ingresar diez pares de números de tres dígitos, crear un nuevo número 
# conformado con la centena del primero y la centena del segundo, luego 
# almacenarlos en un vector D[10]. Imprimir el vector resultante.

import numpy as np

DIM = 10
vector = np.empty(DIM, dtype=int)

# Se realiza la carga de datos en el vector
i = 0
while i < DIM:
    num1 = int(input("Ingrese el primer número del par:"))
    while num1 < 100 or num1 > 999: # Se valida que el número sea de 3 dígitos
        print("El numero ingresado no es de 3 digitos")
        num1 = int(input("Ingrese el primer número del par nuevamente:"))
    num2 = int(input("Ingrese el segundo número del par:"))
    while num2 < 100 or num2 > 999: # Se valida que el número sea de 3 dígitos
        print("El numero ingresado no es de 3 digitos")
        num2 = int(input("Ingrese el segundo número del par nuevamente:"))
    print(" ")
    # Se realiza el calculo para obtener la centena de cada número
    centena1 = num1 // 100
    centena2 = num2 // 100
    aux = centena1 * 10 + centena2
    vector[i] = aux

    i+=1

# Se muestran los datos del vector
print("El vector generado es el siguiente:")
for i in range(0,DIM):
    print(vector[i], end=" ")
print("")
