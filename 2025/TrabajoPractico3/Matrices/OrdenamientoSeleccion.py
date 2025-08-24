import numpy as np

DIMF = 50
DIMC = 6
dimLogF = 4
stock = np.empty([DIMF,DIMC],dtype=int)
stock = np.array(
    [
    [ 1, 3, 5, 9, 6, 7],
    [11,13,15,19,16,17],
    [21,23,25,29,26,27],
    [31,33,35,39,36,37]]
)

i = 0
while i < dimLogF-1:
    p = i
    j = i + 1
    while j < dimLogF:
        # En este condicional el signo "< o >" determina el orden ascendente o descendente
        if stock[j][0] < stock[p][0]:
            p = j
        j += 1
    c = 0
    while c < DIMC:
        aux = stock[p][c]
        stock[p][c] = stock[i][c]
        stock[i][c] = aux
        c = c + 1
    i += 1

print(stock)