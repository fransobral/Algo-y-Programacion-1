pares = 0
numeros = 0
print("Con -1 finalizas el ciclo.")
while numeros != -1:
    numeros = int(input("Ingrese numeros: "))
    if (numeros % 2 == 0):
        pares += 1
print("La cantidad de numeros pares es ", pares)