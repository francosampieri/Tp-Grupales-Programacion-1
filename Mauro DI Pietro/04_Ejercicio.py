lista=(input("Ingrese una lista de numeros seperadas por espacios: "))
lista_numeros=[int(x)for x in lista.split()]
pares=[x for x in lista_numeros if x %2==0]
print(f"La cantidad de pares en la ista son {len(pares)}")