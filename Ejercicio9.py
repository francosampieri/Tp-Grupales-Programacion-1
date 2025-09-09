def primo (numero):
    if numero < 2:
        return False
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True
Lista = input("Ingrese un valor para la lista (separe por espacio cada elemento) ")
Lista_Usuario = Lista.split()
Lista_numeros = [int(x) for x in Lista_Usuario]
Numero_Primos = []
for i in Lista_numeros:
    if primo(i):
        Numero_Primos.append(i)
print(Numero_Primos)