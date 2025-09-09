lista=(input("Ingrese una lista de numeros seperadas por espacios: "))
lista_numeros=[int(x)for x in lista.split()]
indice=int(input("Ingrese el indice del numero que quiere eliminar: "))
del lista_numeros[indice]
print(lista_numeros)