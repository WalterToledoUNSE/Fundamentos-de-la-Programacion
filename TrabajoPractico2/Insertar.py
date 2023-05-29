import numpy as np

DIM_F = 10
n = 5
vectorA = np.empty(DIM_F,dtype=int)
vectorA = np.array([1,2,4,5,6,0,0,0,0,0])

num = int(input("Ingrese el elemento que desea insertar: "))
b = 0
i = 0
while i < n and b == 0:
    # El signo determina el tipo de ordenamiento (ascendente o descendente)
    if num < vectorA[i]:
        j = n
        while j >= i:
            vectorA[j+1] = vectorA[j]
            j -= 1
        vectorA[i] = num
        n += 1
        b = 1
    else:
        i += 1
if b == 0:
    vectorA[i] = num
    n += 1

#Mostrar vectorA
for i in range(0,n):
    print(vectorA[i], end=" ")