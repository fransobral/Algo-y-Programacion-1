#NUMEROS ESCALONADOS
numero = input("ingresa numero")
cantidad_de_numeros_escalonados = 0

lista_repetidos = []
lst = [int(i) for i in str(numero)]
print(lst)
for j in lst:
    if j not in lista_repetidos:
        lista_repetidos.append(j)
    else:
        print("no es escalonado")
        cantidad_de_numeros_escalonados = len(lista_repetidos)
print(cantidad_de_numeros_escalonados)