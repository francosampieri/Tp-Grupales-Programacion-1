numeros = [2 , 4 ,6 ,8 , 10]

factor = int(input("INGRESE UN FACTOR PARA MULTIPLICAR LOS NUMEROS DE LA LISTA : "))


resultado = [num*factor for num in numeros ]


print("Lista Original " , numeros )
print("Lista Multiplicada " , resultado )