7#
#Ejercicio 7: Diagonal de una Matriz Cuadrada 
#Escribe un programa que extraiga los elementos de la diagonal principal de una matriz cuadrada. 
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(matriz)):
    print(matriz[i][i], end= " ")