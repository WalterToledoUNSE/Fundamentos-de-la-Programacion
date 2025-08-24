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

x = int(input("Ingrese el elemento que desea eliminar: "))

i = 0
while i < dimLogF:
    if stock[i][0] == x:
        j = i
        while j < dimLogF-1:
            c = 0
            while c < DIMC:
                stock[j][c] = stock[j+1][c]
                c = c + 1
            j = j + 1
        dimLogF -= 1
    else:
        i += 1

#Mostrar stock
for i in range(0,dimLogF):
    for j in range(0, DIMC):
        print(stock[i][j], end=" ")
    print(" ")