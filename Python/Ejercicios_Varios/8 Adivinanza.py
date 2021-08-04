A = int(input("Escriba un numero: "))
B = int(input("Adivina el numero: "))
nIntentos = 1
while B != A and nIntentos <= 20:

    if B > A:
        print("El numero ingresado es mayor al pedido.")
        nIntentos += 1
    elif B < A:
        print("El numero ingresado es menor al pedido.")
        nIntentos += 1
    B = int(input("Adivina el numero: "))
    
if B == A:
    print("Acertaste el numero! Muy bien!")
    if nIntentos > 1:
        print(f"Te tomo {nIntentos} intentos!")
    else:
        print(f"Te tomo {nIntentos} intento!")
else:
    print("Superaste los 20 intentos.")
    