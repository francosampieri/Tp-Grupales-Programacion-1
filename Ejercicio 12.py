#Escribe un programa que sume dos listas de números elemento por elemento. Las listas deben tener la misma longitud. 
lista_uno = [1, 2, 3, 4, 5]
lista_dos = [10, 9, 8, 7, 6]
lista_sumada = []
for i in range(len(lista_uno)):
    lista_sumada.append(lista_uno[i] + lista_dos[i])
for i in range(len(lista_sumada)): print(f"{lista_uno[i]} + {lista_dos[i]} = {lista_sumada[i]}")