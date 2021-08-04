
'''
Realizar un programa que permita jugar a adivinar un número entero. 
El participante A elige el número a adivinar, y luego hace jugar al participante B, el cual deberá intentar adivinarlo arriesgando números. 
El programa debe guiar al participante B indicándole, en cada intento, si el número arriesgado es mayor o menor al definido por el participante A.
El juego debe concluir al acertar el número o superar los 20 intentos. 
Al acertar el número debe indicar la cantidad de intentos que fueron utilizados para lograrlo. 
En caso de no haber conseguido el objetivo, debe indicarle que ha superado los 20 intentos.
'''
nuermo_adivinar = int(input("Por favor ingrese un numero: "))
intentos = 0
intento = "no"
while intento != nuermo_adivinar and intentos < 20:
    intentos += 1    
    intento = int(input("Ingrese su adivinanza: "))
if intento == nuermo_adivinar:
    print(f"Has ganado el juego con {intentos} intentos.")
else:
    print("Superaste los 10 inentos. Perdiste")