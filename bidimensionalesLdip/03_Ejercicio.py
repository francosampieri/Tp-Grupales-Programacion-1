matriz=[
    [123,50,20],
    [20,30,87],
    [50,65,78]
]
suma_total=sum(sum(i)for i in matriz)
suma_fila1=sum(matriz[0])
print(f"La suma de la fila 1 es: {suma_fila1}")
suma_fila2=sum(matriz[1])
print(f"La suma de la fila 2 es: {suma_fila2}")
suma_fila3=sum(matriz[2])
print(f"La suma de la fila 3 es: {suma_fila3}")
print(f"La suma total es: {suma_total}")