#Multiplicacion de una Matriz por un Escalar

filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))

matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        num = float(input(f"Ingrese el elemento [{i+1},{j+1}]: "))
        fila.append(num)
    matriz.append(fila)

escalar = float(input("Ingrese el valor escalar: "))

matriz_resultado = []
for i in range(filas):
    fila_resultado = []
    for j in range(columnas):
        fila_resultado.append(matriz[i][j] * escalar)
    matriz_resultado.append(fila_resultado)

print("\nMatriz resultante:")
for fila in matriz_resultado:
    print(fila)
