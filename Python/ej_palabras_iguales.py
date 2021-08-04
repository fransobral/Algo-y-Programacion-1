
palabra_inicial = "caso"
p1 = "mama"
p2 = "clase"
p3 = "cosa"
p4 = "saco"
p5 = "pepe"


def separar_palabras(palabra:str) -> list:
    palabra_list = list()
    for letra in palabra:
        palabra_list.append(letra)
    return palabra_list

p_inicial_separada = separar_palabras(palabra_inicial)
p_inicial_separada.sort()
p1_separada = separar_palabras(p1)
p1_separada.sort()
p2_separada = separar_palabras(p2)
p2_separada.sort()
p3_separada = separar_palabras(p3)
p3_separada.sort()
p4_separada = separar_palabras(p4)
p4_separada.sort()
p5_separada = separar_palabras(p5)
p5_separada.sort()

if p_inicial_separada == p1_separada:
    print(p1)
if p_inicial_separada == p2_separada:
    print(p2)
if p_inicial_separada == p3_separada:
    print(p3)
if p_inicial_separada == p4_separada:
    print(p4)
if p_inicial_separada == p5_separada:
    print(p5)
