numero = int(input("Ingrese el tamaño de la matriz "))
matriz = []
for i in range(numero):
    fila = [0] * numero
    matriz.append(fila)
for i in range(numero):
    matriz[i][i] = 1
for fila in matriz:
    print(fila)