def orden_numeros(cadena:str) -> str:
    lista_ppal = list()
    
    for numero in cadena:
        numero = int(numero)
        lista_ppal.append(numero)

    once = set()
    seenOnce = once.add
    repetidos = list( num for num in lista_ppal if num in once or seenOnce(num))

    for num in range(len(repetidos)):
        if not repetidos[num] % 2 == 0:
            repetidos[num] = repetidos[num] -1
    
    lista_ppal.sort()
    repetidos.sort()
    lista_ppal.extend(repetidos)
    for i in range(len(lista_ppal)):
        lista_ppal[i] = str(lista_ppal[i])
    
    lista_ppal = "".join(lista_ppal)

    return print(lista_ppal)


def main() -> None:
    orden_numeros("1364522377")

main()


