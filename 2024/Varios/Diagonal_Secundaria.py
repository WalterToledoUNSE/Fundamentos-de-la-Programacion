import numpy as np

DIM = 5
matriz = np.empty(DIM,dtype=int)
matriz = np.array([
    [1,2,3,4,5],
    [10,20,30,40,50],
    [6,7,8,9,10],
    [60,70,80,90,100],
    [30,31,32,33,34]
])

j = DIM-1
for i in range(DIM):
    j = DIM - 1 - i
    print("El elemento es: ", matriz[i][j])
    # j = j - 1

