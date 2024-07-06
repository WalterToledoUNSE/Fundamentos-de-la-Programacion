import numpy as np

DIM_F = 10
n = 5
vectorA = np.empty(DIM_F,dtype=int)
vectorA = np.array([1,4,6,8,10,0,0,0,0,0])

#Mostrar vectorA
for i in range(0,n):
    print(vectorA[i], end=" ")
print("")

num = int(input("Ingrese el numero a buscar: "));
pri = 0
ult = n
med = (pri + ult) // 2 # División tomando la parte entera
while ((pri <= ult) and (num != vectorA[med])):
    if (num < vectorA[med]):
        ult = med - 1
    else:
        pri = med + 1
    med = (pri + ult) // 2 # División tomando la parte entera
if (pri <= ult):
    print("El número",num,"fue encontrado...\n")
else:
    print("El número",num,"no fue encontrado...\n")
