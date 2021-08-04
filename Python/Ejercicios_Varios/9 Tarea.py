nRonda = 0
numeros = 0
suma = 0
print("Con -1 dejas de ingresar numeros.")
for i in range(9):
    nRonda += 1
    print(f"Ronda {nRonda}:")
    while numeros != -1:
        numeros = int(input("Ingrese todos los numeros: "))
        suma += numeros
        print(suma)
    



