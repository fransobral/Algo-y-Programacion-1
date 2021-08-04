""""
(El ejercicio se llama: ODIO A LOS IMPARES) Crear un programa que:
Permita ingresar 5 números enteros positivos.
Calcule el máximo entre esos números; lo muestre.
Calcule el mínimo; lo muestre.
Calcule el promedio; lo muestre.
Sume el máximo, el mínimo; y el promedio (Resultando en un entero. Para eso pueden castear el resultado a int. 
Ejemplo: int(resultado)) y en caso de que el resultado sea par; salude al usuario tantas veces como número resultante de esa cuenta, 
si es impar; vuelve a empezar TODO el programa DE NUEVO.

"""
def programa1()-> None:
    numero = 0
    cantidadint = 0
    maximo = 0
    minimo = 1000000
    valoresN = 0

    while cantidadint != 5:
        numero = int((input("Ingrese un numero positivo: ")))
        if numero <= 0:
            print("Ese numero no es positivo, intente nuevamente.")
        else:
            cantidadint += 1
            valoresN += numero
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

    promedio = int((valoresN/5))

    print(f"El maximo es de {maximo}.")
    print(f"El minimo es de {minimo}.")
    print(f"El promedio es de {promedio}.")

    suma_todo = int(maximo + minimo + promedio)

    if suma_todo % 2 == 0:
        for i in range(1,suma_todo):
            print('Hola usuario!')
    else:
        programa1()

programa1()




