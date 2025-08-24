import numpy as np

DIM = 10
vectorA = np.empty(DIM,dtype=int)
vectorA = np.array([34, 56, 23, 78, 12, 1, 99, 3, 45, 89])

#Mostrar vectorA
print("El vector original es el siguiente:")
for i in range(0,DIM):
    print(vectorA[i], end=" ")
print("")

i = DIM
b = 1
while b != 0:
    b = 0
    j = 0
    while j<i-1:
        # En este condicional el signo "< o >" determina el orden ascendente o descendente
        if vectorA[j] > vectorA[j+1]:
            aux = vectorA[j]
            vectorA[j] = vectorA[j+1]
            vectorA[j+1] = aux
            b = 1
        j += 1
    i -= 1

#Mostrar vectorA
print("El vector ordenado es el siguiente:")
for i in range(0,DIM):
    print(vectorA[i], end=" ")
print("")