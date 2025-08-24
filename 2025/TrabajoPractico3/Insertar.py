import numpy as np

DIMF = 10
DIMC = 6
dimLogF = 4
stock = np.empty([DIMF,DIMC],dtype=int)
stock = np.array([
    [ 1, 3, 5, 9,20,20],
    [11,13,15,19,20,20],
    [21,23,25,29,20,20],
    [31,33,35,39,20,20],
    [ 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0],
])

num = int(input("Ingrese el elemento que desea insertar: "))
b = 0
i = 0
while i < dimLogF and b == 0:
    # El signo determina el tipo de ordenamiento (ascendente o descendente)
    if num < stock[i][0]:
        j = dimLogF-1
        while j >= i:
            c = 0
            while c < DIMC:
                stock[j+1][c] = stock[j][c]
                c = c + 1
            j -= 1
        stock[i][0] = num
        stock[i][1] = 0
        stock[i][2] = 0
        stock[i][3] = 0
        stock[i][4] = 0
        stock[i][5] = 0
        dimLogF += 1
        b = 1
    else:
        i += 1
if b == 0:
    stock[i][0] = num
    stock[i][1] = 0
    stock[i][2] = 0
    stock[i][3] = 0
    stock[i][4] = 0
    dimLogF += 1

# #Mostrar stock
for i in range(0,dimLogF):
    for j in range(0, DIMC):
        print(stock[i][j], end=" ")
    print("")