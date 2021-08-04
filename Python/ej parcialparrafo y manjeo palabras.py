'''
Dada una cadena que contiene un párrafo, se pide:
a.Crear una función que reciba el párrafo y devuelva todas las palabras ordenadas alfabéticamente en forma descendente.
b.Crear una función que reciba el párrafo y devuelva la cantidad total de palabras
c.Crear una función que reciba el párrafo y una lista de palabras prohibidas. Dicha función deberá devolver el párrafo con las palabras prohibidas reemplazadas por **** (cuatro asteriscos)
'''

parrafo = """
Dada una cadena que contiene un párrafo, se pide:
a.Crear una funcion que reciba el párrafo y devuelva todas las palabras ordenadas alfabéticamente en forma descendente.
b.Crear una funcion que reciba el párrafo y devuelva la cantidad total de palabras
c.Crear una funcion que reciba el párrafo y una lista de palabras prohibidas. Dicha función deberá devolver el párrafo con las palabras prohibidas reemplazadas por **** (cuatro asteriscos)
"""


def orden_palabras(parrafo):
    palabras = parrafo.split(" ")
    print(palabras)


def cantidad_palabras(parrafo):
    palabras = parrafo.split(" ")
    print(f"En total hay {len(palabras)} palabras.")


def palabras_prohibidas(parrafo):
    parrafo = parrafo.replace("funcion","****")

    print(parrafo)


