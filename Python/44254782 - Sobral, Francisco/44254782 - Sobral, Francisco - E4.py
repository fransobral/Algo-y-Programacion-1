def calculador_numeros(numeros:str) -> tuple:
    numeros_lista = numeros.split(" ")
    lista_int = list()
    suma_total = 0
    for numero in numeros_lista:
        lista_int.append(int(numero))

    maximo = max(lista_int)
    minimo = min(lista_int)

    for numero in lista_int:
        suma_total += numero

    return maximo,minimo,suma_total

def main()-> None:
    numeros = "2 76 5 43 5 7 8 23"
    maximo,minimo,suma_total = calculador_numeros(numeros)
    print(f"El maximo numero es el {maximo}, el minimo es el {minimo}, y por ultimo, la suma total es de {suma_total}.")
main()