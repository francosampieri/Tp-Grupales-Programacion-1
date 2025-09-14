def validar_nat_rango(mensaje,rango = None):
    num = input(mensaje)
    if rango != None:
        while not num.isnumeric() or int(num) not in range(rango[0],rango[1]+1): #valida primero si es un numero y despues si esta en el rango
            print("ERROR: Ingresa un numero entero dentro del rango")
            num = input(mensaje)
    else:
        while not num.isnumeric():
            print("ERROR: Ingresa un numero entero")
            num = input(mensaje)
    return int(num)

def menu_practico_uno(funciones):
    """Menu para seleccionar ejercicios\n
    Recibe list con las funciones de cada ejercicio empezando por None
    """
    seguir = True
    while seguir:
        print("-----PRACTICO 1-----")
        ejercicio_elegido = validar_nat_rango(f"Ingrese el numero de ejercicio que desea ejecutar (1-{len(funciones)-1}) [0] para volver ", [0, len(funciones)-1])
        if ejercicio_elegido == 0: 
            seguir = False
            continue
        else: 
            print(f"\n -----EJERCICIO {ejercicio_elegido}-----")
            funciones[ejercicio_elegido]()
            print() #salto de linea
            input("Presione ENTER para volver") #para no sobrecargar consola

def menu_practico_dos(funciones):
    """Menu para seleccionar ejercicios\n
    Recibe list con las funciones de cada ejercicio empezando por None
    """
    seguir = True
    while seguir:
        print("-----PRACTICO 2-----")
        ejercicio_elegido = validar_nat_rango(f"Ingrese el numero de ejercicio que desea ejecutar (1-{len(funciones)-1}) [0] para volver ", [0, len(funciones)-1])
        if ejercicio_elegido == 0: 
            seguir = False
            continue
        else: 
            print(f"\n -----EJERCICIO {ejercicio_elegido}-----")
            funciones[ejercicio_elegido]()
            print() #salto de linea
            input("Presione ENTER para volver") #para no sobrecargar consola

def menu():
    funciones_1 = [None, ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5, ejercicio_6, ejercicio_7, ejercicio_8, ejercicio_9, ejercicio_10, ejercicio_11, ejercicio_12, ejercicio_13]
    funciones_2 = [None, ejercicio_2_1, ejercicio_2_2, ejercicio_2_3, ejercicio_2_4, ejercicio_2_5, ejercicio_2_6, ejercicio_2_7, ejercicio_2_8, ejercicio_2_9, ejercicio_2_10, ejercicio_2_11]

    seguir = True
    while seguir:
        practico_elegido = validar_nat_rango("Ingrese el practico que desea ejecutar (1 ó 2) [0 para terminar] ", (0,2))
        if practico_elegido == 0:
            seguir = False
            continue
        elif practico_elegido == 1: menu_practico_uno(funciones_1)
        else: menu_practico_dos(funciones_2)

def ejercicio_1():
    nums_list = input("Ingresa una lista de números separados por espacios: ")
    lista_numeros = [int(num) for num in nums_list.split()]

    suma = 0
    for numero in lista_numeros:
        suma += numero

    print("La suma de los elementos es:", suma)

def ejercicio_2():
    lista = (input ("Introduce una lista de numeros separados por un espacio "))
    numeros = [int(num) for num in lista.split()]
    numero_mayor = numeros[0]
    numero_menor = numeros[0]
    for num in numeros:
        if num > numero_mayor:
            numero_mayor = num
        if num < numero_menor:
            numero_menor = num

    print (f"Numero mayor de la lista {numero_mayor} ")
    print (f"Numero menor de la lista {numero_menor} ")

def ejercicio_3():
    lista = input("Ingrese una lista de numeros separados por un espacio ")
    lista_usuario = lista.split()
    lista_invertida = []
    for i in range(len(lista_usuario)-1,-1,-1):
        lista_invertida.append(lista_usuario[i])
    print("Lista Original", lista_usuario)
    print("Lista Invertida", lista_invertida)

def ejercicio_4():
    lista=(input("Ingrese una lista de numeros separados por espacios: "))
    lista_numeros=[int(x)for x in lista.split()]
    pares=[x for x in lista_numeros if x %2==0]
    print(f"La cantidad de pares en la lista es {len(pares)}")

def ejercicio_5():
    numeros = [2, 4, 6, 8, 10]
    factor = int(input("INGRESE UN FACTOR PARA MULTIPLICAR LOS NUMEROS DE LA LISTA: "))
    resultado = [num*factor for num in numeros]
    print("Lista Original", numeros )
    print("Lista Multiplicada", resultado )

def ejercicio_6():
    lista_numeros = input("Ingresa una lista de numeros separados por un espacio ").split()
    lista_numeros = list(set(lista_numeros)) #al pasarlo por set elimina los duplicados
    print(f"Lista sin duplicados: {lista_numeros}")

def ejercicio_7():
    nums = input("Ingresa una lista de números separados por espacios: ")
    lista_num = [int(num) for num in nums.split()]

    suma = 0
    for n in lista_num: suma += n

    promedio = suma / len(lista_num)
    print("El promedio de los elementos es:", promedio)

def ejercicio_8():
    lista_repetidos= ("manzana","banana","melon","sandia","manzana","mandarina")
    conteo = {}
    for i in lista_repetidos:
        if i in conteo:
            conteo[i] += 1
        else:
            conteo[i] = 1
    print(f"Lista inicial: {lista_repetidos}")
    for elemento in conteo.items():
        if elemento[1]>1:
            print(f"{elemento[0]} aparece {elemento[1]} veces")

def ejercicio_9():
    def primo (numero):
        if numero < 2:
            return False
        for i in range(2,(numero//2)+1):
            if numero % i == 0:
                return False
        return True
    
    lista = input("Ingrese una lista de numeros separados por espacios para saber cuales son primos ")
    lista_usuario = lista.split()
    lista_numeros = [int(x) for x in lista_usuario]
    numero_primos = []
    for i in lista_numeros:
        if primo(i):
            numero_primos.append(i)
    print(f"Numeros primos: {numero_primos}")

def ejercicio_10():
    lista=(input("Ingrese una lista de numeros separados por espacios: "))
    lista_numeros=[int(x)for x in lista.split()]
    indice=validar_nat_rango("Ingrese el indice del numero que quiere eliminar: ")
    lista_numeros.pop(indice)
    print(lista_numeros)

def ejercicio_11():
    entrada = input("Ingrese un lista de numero separados por espacios: ")
    numeros = [int(x) for x in entrada.split()]
    buscado = int(input("Ingrese el numero que desea buscar "))
    
    cantidad = 0
    for num in numeros:
        if num == buscado:
            cantidad += 1

    print(f"El numero {buscado} aparece {cantidad} veces.")

def ejercicio_12():
    lista_uno = [1, 2, 3, 4, 5]
    lista_dos = [10, 9, 8, 7, 6]
    lista_sumada = []
    for i in range(len(lista_uno)):
        lista_sumada.append(lista_uno[i] + lista_dos[i])
    print(f"Lista 1:\n{lista_uno}\nLista 2:\n{lista_dos}")
    for i in range(len(lista_sumada)): print(f"{lista_uno[i]} + {lista_dos[i]} = {lista_sumada[i]}")

def ejercicio_13():
    print("NumPy es fundamental para manejar matrices y arrays en python por las siguientes caracteristicas:\nManeja arrays y matrices multidisionales de manera comoda.\nIncluye una gran variedad de funciones matematicas utiles y de algebra lineal.\nEs mucho mas eficiente en memoria que las listas de python.")
    print("EJEMPLOS")
    import numpy as np
    arr = np.array([10, 20, 30, 40])
    matriz = np.array([[1, 2], 
                    [3, 4]])
    print("Array:", arr)
    print("Matriz:\n", matriz)

def ejercicio_2_1():
    matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

    suma_total = 0
    print("MATRIZ ORIGINAL", end="")
    for fila in matriz:
        print() #salto de linea
        for num in fila:
            print(num, end="")
            suma_total += num
    print()
    print(f"La suma total de los numeros es: {suma_total}")

def ejercicio_2_2():
    matriz=[
    [123,50,20],
    [20,30,87],
    [50,65,78]]
    
    suma_total=0
    for fila in matriz:
        for elemento in fila:
            suma_total += elemento

    print(f"La suma total de la matriz {matriz} es : {suma_total}")

def ejercicio_2_3():
    matriz=[
        [123,50,20],
        [20,30,87],
        [50,65,78]
    ]
    suma_total=0
    suma_fila1=0
    suma_fila2=0
    suma_fila3=0
    for fila in matriz:
        for elemento in fila:
            suma_total += elemento
    for elemento in matriz[0]:
        suma_fila1 += elemento
    print(f"La suma de la fila 1 es: {suma_fila1}")
    for elemento in matriz[1]:
        suma_fila2 += elemento
    print(f"La suma de la fila 2 es: {suma_fila2}")
    for elemento in matriz[2]:
        suma_fila3 += elemento
    print(f"La suma de la fila 3 es: {suma_fila3}")
    print(f"La suma total es: {suma_total}")

def ejercicio_2_4():
    matriz = [
    [1, 2],
    [3, 4],
    [5, 6]]
    transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    print(transpuesta)

def ejercicio_2_5():
    lista_bidimensional = [[0,1,28],[0,10,4],[20,-5,21]]
    mayor = lista_bidimensional[0][0] #inicializar
    print("MATRIZ")
    for filas in lista_bidimensional:
        print(filas)
        for elementos in filas:
            if elementos > mayor: mayor = elementos
    
    print("El mayor numero de la matriz es", mayor)

def ejercicio_2_6():
    filas = validar_nat_rango("Ingrese la cantidad de filas de la matriz: ")
    columnas = validar_nat_rango("Ingrese la cantidad de columnas de la matriz: ")
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

def ejercicio_2_7():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    for i in range(len(matriz)):
        print(matriz[i][i], end= " ")
    print() #salto de linea

def ejercicio_2_8():
    numero = validar_nat_rango("Ingrese el tamaño de la matriz ")
    matriz = []
    for i in range(numero):
        fila = [0] * numero
        matriz.append(fila)
    for i in range(numero):
        matriz[i][i] = 1
    for fila in matriz:
        print(fila)

def ejercicio_2_9():
    numero = validar_nat_rango("Ingrese el tamaño de la matriz ")
    matriz = []
    for i in range(numero):
        fila = [0] * numero
        matriz.append(fila)
    for i in range(numero):
        matriz[i][numero -1 -i] = 1
    for fila in matriz:
        print(fila)

def ejercicio_2_10():
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

def ejercicio_2_11():
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    print("MATRIZ ORIGINAL")
    for filas in matriz:
        if filas != matriz[0]: print()
        for columnas in filas:
            print(columnas, end="")
    print("\n")
    print("MATRIZ GIRADA 90º")

    matriz_reversa = []
    #revierte la matriz sin .reverse()
    for i in range(len(matriz)-1, -1, -1):  #recorre la matriz desde su ultima fila hacia atras
        matriz_reversa.append(matriz[i])

    #imprime la matriz intercambiando columnas y filas
    for i in range(len(matriz_reversa)):
        if i != 0: print()
        for j in range(len(matriz_reversa[0])):
            print(matriz_reversa[j][i], end="")

#main
menu()