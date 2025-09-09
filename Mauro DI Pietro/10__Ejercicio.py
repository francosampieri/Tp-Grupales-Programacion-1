lista_numeros=[]
for i in range (5):
    numero=int(input("Ingrese un numero "))
    lista_numeros.append(numero)
indice=int(input("Ingrese el indice del numero que quiere eliminar"))
del lista_numeros[indice]
print(lista_numeros)