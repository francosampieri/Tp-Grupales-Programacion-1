#Promedio de una lista

nums = input("Ingresa números separados por espacios: ")

lista_num = [int(num) for num in nums.split()]

if len(lista_num) > 0:
    promedio = sum(lista_num) / len(lista_num)
    print("El promedio de los elementos es:", promedio)
else:
    print("Ingrese un numero")
