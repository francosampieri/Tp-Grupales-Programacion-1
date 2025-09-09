# hago una funcion para ver si es simetrica 
def es_simetrica(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    # una matriz tiene que ser cuadrada para que sea simetrica (por eso corroboro eso )

    if filas != columnas:
        return False

    # Comparo si son iguales a su transpuestas
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

matriz = [
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
]

if es_simetrica(matriz):
    print("La matriz es simétrica")
else:
    print("La matriz NO es simétrica")
