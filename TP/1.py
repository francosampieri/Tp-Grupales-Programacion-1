#Suma de elementos

nums_list = input("Ingresa números separados por espacios: ")

lista_numeros = [int(num) for num in nums_list.split()]

suma = sum(lista_numeros)

print("La suma de los elementos es:", suma)
