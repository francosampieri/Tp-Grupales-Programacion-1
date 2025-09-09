<<<<<<< HEAD
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

        
=======
entrada = input("Ingrese un lista de numero separados por comas: ")

numeros = [int(x) for x in entrada.split(",")]

buscado = int(input("Ingrese el numero que desea buscar "))


cantidad = numeros.count(buscado)


print(f"El numero {buscado} aparece una cantidad de {cantidad} veces. ")

>>>>>>> d4409fb37346e1d230fcd38498749477aa23c343
