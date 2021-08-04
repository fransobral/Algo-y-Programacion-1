n = int(input("Ingrese un número: "))
for dividendo in range(1, n+1):
    suma_divisores = 0
    for divisor in range(1, dividendo):
        if dividendo % divisor == 0:
            suma_divisores += divisor
    if suma_divisores == dividendo:
        print(f"{dividendo} es número perfecto.")