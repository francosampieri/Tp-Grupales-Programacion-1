#Escribe un programa que gire una lista bidimensional (matriz) 90 grados en el sentido de las agujas del reloj.
matriz = [[1,2,3],[4,5,6],[7,8,9]]
print("MATRIZ ORIGINAL")
for filas in matriz:
    if filas != matriz[0]: print()
    for columnas in filas:
        print(columnas, end="")

print("\n")
print("MATRIZ GIRADA 90º")
matriz.reverse()
for i in range(len(matriz)):
    if i != 0: print()
    for j in range(len(matriz[0])):
        print(matriz[j][i], end="")

        