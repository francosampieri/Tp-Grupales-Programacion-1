#Escribe un programa que permita al usuario ingresar una lista de números y elimine los elementos duplicados. 
lista_numeros = input("Ingresa una lista de numeros separados por un espacio ").split()
lista_numeros = list(set(lista_numeros))
print(lista_numeros)