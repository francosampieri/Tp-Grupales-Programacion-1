entrada = input("Ingrese un lista de numero separados por comas: ")

numeros = [int(x) for x in entrada.split(",")]

buscado = int(input("Ingrese el numero que desea buscar "))


cantidad = numeros.count(buscado)


print(f"El numero {buscado} aparece una cantidad de {cantidad} veces. ")

