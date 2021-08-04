def orden_numeros(cadena:str) -> str:
    cadena_separada = list()
    pares = list()
    pares_no_repetidos = list()
    pares_repetidos = list()
    impares = list()
    impares_no_repetidos = list()
    impares_repetidos = list()

    for numero in cadena:
        numero = int(numero)
        cadena_separada.append(numero)

    for i in range(len(cadena_separada)):  
        if cadena_separada[i] % 2 == 0:
            pares.append(cadena_separada[i])
        else:
            impares.append(cadena_separada[i])

    for i in range(len(pares)):
        if pares[i] not in pares_no_repetidos:
            pares_no_repetidos.append(pares[i])
        else:
            pares_repetidos.append(pares[i])
    
    for i in range(len(impares)):
        if impares[i] not in impares_no_repetidos:
            impares_no_repetidos.append(cadena_separada[i])
        else:
            impares_repetidos.append(cadena_separada[i]-1)

    cadena_separada.sort()
    impares_repetidos.extend(pares_repetidos)
    impares_repetidos.sort()
    cadena_separada.extend(impares_repetidos)
    
    print(cadena_separada)

def main() -> None:
    orden_numeros("136452237")

main()



    


