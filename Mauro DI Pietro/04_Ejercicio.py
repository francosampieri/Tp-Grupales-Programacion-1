lista_numeros=[]
for i in range (5):
    numero=int(input("Ingrese un numero "))
    lista_numeros.append(numero)
pares=[x for x in lista_numeros if x %2==0]
print(f"La cantidad de pares en la ista son {len(pares)}")