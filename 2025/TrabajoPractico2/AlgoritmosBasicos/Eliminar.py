import numpy as np

DIM_F = 6 # Dimensión Física
dim = DIM_F # Dimensión Lógica
vectorA = np.empty(DIM_F,dtype=int)
vectorA = np.array([1,2,3,2,5,6])

#Mostrar vectorA
print("El vector definido es el siguiente:")
for i in range(0,dim):
    print(vectorA[i], end=" ")
print("")

x = int(input("Ingrese el elemento que desea eliminar: "))
i = 0
while i < dim:
    if vectorA[i] == x:
        j = i
        while j < dim-1:
            vectorA[j] = vectorA[j+1]
            j = j + 1
        dim -= 1
    else:
        i += 1

print("El vector resultante es el siguiente:")
#Mostrar vectorA
for i in range(0,dim):
    print(vectorA[i], end=" ")