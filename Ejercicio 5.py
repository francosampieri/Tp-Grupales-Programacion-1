#Escribe un programa que encuentre el valor más grande en una lista bidimensional.
lista_bidimensional = [[0,1,8],[0,190,4],[100,-5,21]]
mayor = max(max(lista_bidimensional[0]), max(lista_bidimensional[1]), max(lista_bidimensional[2]))
print(mayor)