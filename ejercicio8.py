8#
#Escribe un programa que identifique y muestre los elementos que se repiten en una lista. 
#Pista: 
#Utiliza un diccionario o un conjunto (set) para hacer el seguimiento de los elementos. 
lista_repetidos= ("manzana","banana","melon","sandia","manzana","mandarina")
conteo = {}
for i in lista_repetidos:
    if i in conteo:
        conteo[i] += 1
    else:
        conteo[i] = 1
print(conteo)
for elemento in conteo.items():
    if elemento[1]>1:
        print(elemento)
    conteo.get