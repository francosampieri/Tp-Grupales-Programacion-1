lista = (input ("introduce una lista de numeros separados por coma "))
numeros = [float(num.strip()) for num in lista.split(",")]
numero_mayor = max(numeros)
numero_menor = min(numeros)
print (f"numero mayor de la lista {numero_mayor} ")
print (f"numero menor de la lista {numero_menor} ")
