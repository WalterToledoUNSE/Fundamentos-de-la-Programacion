import numpy as np


def generarMatrizBase(tablero, DIM):
    """
    Genera una matriz 9x9 que cumple con las reglas básicas de un Sudoku:
    - Cada fila contiene los números del 1 al 9 sin repetir.
    - Cada columna contiene los números del 1 al 9 sin repetir.
    - Se construye a partir de la primera fila aleatoria y desplazamientos sistemáticos.

    Returns:
        matriz (np.ndarray): Matriz 9x9 con valores del 1 al 9.
    """

    # Generar primera fila como una permutación aleatoria de los números 1 a 9
    tablero[0] = np.random.permutation(np.arange(1, 10))

    # Construcción de filas restantes usando desplazamientos (np.roll)
    # Patrón de desplazamientos: 3, 3, 1 para generar un cuadrado latino
    for i in range(1, DIM):
        if i % 3 == 0:
            # Cada 3 filas se desplaza en 1 posición a la derecha
            tablero[i] = np.roll(tablero[i - 1], 1)
        else:
            # En el resto de las filas se desplaza en 3 posiciones a la derecha
            tablero[i] = np.roll(tablero[i - 1], 3)

    return None


def generar_tablero_con_pistas(tablero, DIM, cantidad_pistas):
    """
    Genera un tablero de Sudoku inicial con cierta cantidad de pistas.
    Las celdas no incluidas en las pistas se reemplazan por 0.

    Args:
        cantidad_pistas (int): Número de celdas que permanecerán visibles.
                              Valores típicos:
                                - 40+ pistas = tablero fácil
                                - 30-40 pistas = tablero intermedio
                                - <30 pistas = tablero difícil

    Returns:
        tablero (np.ndarray): Matriz 9x9 con algunas celdas visibles y otras en 0.
        matriz_base (np.ndarray): Solución completa del tablero (sin ceros).
    """
    # Generar matriz base (solución completa)
    generarMatrizBase(tablero,DIM)
    # tablero = np.copy(matriz_base)  # Copia para no alterar la matriz original

    # Generar array con las posiciones de todas las celdas (0 a 80)
    posiciones = np.arange(81)
    np.random.shuffle(posiciones)  # Barajar posiciones para eliminar al azar

    # Calcular cuántas celdas se deben vaciar
    celdas_a_eliminar = 81 - cantidad_pistas

    # Reemplazar por 0 las celdas seleccionadas para vaciar
    for k in range(celdas_a_eliminar):
        pos = posiciones[k]
        fila, col = divmod(pos, DIM)  # Convertir índice lineal a fila y columna. Ejemplo: A[0] = A[0][0] y A[1] = A[0][1]
        tablero[fila, col] = 0  # Asignar 0 (celda vacía)

    return None


DIM = 9
matriz = np.zeros((DIM, DIM), dtype=int)  # Matriz inicial llena de ceros
generar_tablero_con_pistas(matriz,DIM,65)

# Mostrar resultados
print("Tablero inicial (0 = celda vacía):")
print(matriz)

