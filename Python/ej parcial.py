""" def ingreso_usuario():
    dni = input("Ingrese su DNI: ")
    nombre = input("Ingrese su Nombre y Apellido: ")
    cantidad_asistencias = input("Ingrese cantidad de veces asistidas: ")
    tratamientos_realizados = input("Ingrese sus tratamientos realizados separados por coma: ")
    tratamientos_realizados = tratamientos_realizados.split(",")
    datos_usuario = {"DNI":dni,"Nombre":nombre,"Cantidad_asistencias":cantidad_asistencias, "Tartamientos_realizados":tratamientos_realizados}
    return datos_usuario


def repetidos(lista):
    for i in lista:
        cant = lista.count(i)
    return print(cant)

lis = ["matias","juan","matias","matias","fran"]

repetidos(lis) """


def validacion_numero(numero:str) -> int:
    while not numero.isnumeric():
        print("\nEse numero no es valido, intenta nuevamente.\n")
        numero = input("Ingrese un numero mayor a 10: ")
    numero = int(numero)
    if numero <= 10:
        print("\nEse numero no es valido, intenta nuevamente.\n")
        numero = input("Ingrese un numero mayor a 10: ")
    
    return str(numero)

def verificar_escalonado(numero:str)-> int:
    numero = numero.split()
    numero_ordenado = numero.sorted  ()
    if numero == numero_ordenado:
        cantidad = len(numero_ordenado)
        print(f"Es escalonado, {cantidad}.")
    else:
        print("No es escalonado.")

eleccion_numero = input("Ingrese un numero mayor a 10: ")
eleccion_numero = validacion_numero(eleccion_numero)
verificar_escalonado(eleccion_numero)