#Para sumar todos los elementos de una lista bidimensional, puedes usar un bucle anidado o una comprensión de listas. 
#suma_total = sum(sum(fila) for fila in matriz) print(suma_total) 
#Aquí, sum(fila) suma todos los elementos de cada fila, y luego sum() suma los resultados para obtener la suma total de la matriz. 
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Suma todos los elementos de la matriz
suma_total = sum(sum(fila) for fila in matriz)

print(suma_total)
