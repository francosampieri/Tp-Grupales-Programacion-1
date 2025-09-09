Lista = input("Ingrese un valor para la lista (separe por espacio cada elemento) ")
Lista_Usuario = Lista.split()
Lista_Invertida = []
for i in range(len(Lista_Usuario)-1,-1,-1):
    Lista_Invertida.append(Lista_Usuario[i])
print("Lista Original", Lista_Usuario)
print("Lista Invertida", Lista_Invertida)