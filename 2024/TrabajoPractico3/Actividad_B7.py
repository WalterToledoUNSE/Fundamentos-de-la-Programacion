import numpy as np

def cargarMatriz(M):
    M[0][0] = 15
    M[0][1] = 23
    M[0][2] = 56
    M[0][3] = 22
    M[0][4] = 98
    M[1][0] = 25
    M[1][1] = 99
    M[1][2] = 28
    M[1][3] = 39
    M[1][4] = 37
    M[2][0] = 44
    M[2][1] = 66
    M[2][2] = 74
    M[2][3] = 73
    M[2][4] = 59
    M[3][0] = 69
    M[3][1] = 63
    M[3][2] = 61
    M[3][3] = 60
    M[3][4] = 37
    M[4][0] = 87
    M[4][1] = 72
    M[4][2] = 22
    M[4][3] = 13
    M[4][4] = 11

    dim = 5
    return  dim
def mostrarMatriz(M,dimF,dimC):
    for i in range(0, dimF):
        for j in range(0, dimC):
            print(M[i][j], end=" ")
        print("")
    return None
def mostrarTriangularSuperior(M,dimF,dimC):
    print("La Triangular superior es:")
    for i in range(0, dimF):
        for j in range(0, dimC):
            if i < j:
                print(M[i][j], end=" ")
        print("")
    return None

# Programa Principal

N = 6
#declaro la matriz
matriz = np.empty((N,N),dtype=int)

orden = cargarMatriz(matriz)
dimF = orden
dimC = orden
mostrarMatriz(matriz,dimF,dimC)
mostrarTriangularSuperior(matriz, dimF, dimC)