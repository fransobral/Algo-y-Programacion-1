'''
Calculadora de matrices cuadradas.

Crear un programa que primero cree dos matrices identidad de NxN, con un N determinado por el usuario. Si el usuario
quiere cerrar el programa debe de existir una opción para eso. !
Una vez creadas las matrices, se debe desplegar un nuevo menú para operar con las matrices A y B.
    1.Modificar A y B !
    2.Mostrar en pantalla las matrices actuales !
    3.Sumar A + B y mostrar en pantalla la matriz resultante !
    4.Multiplicar A + B y mostrar en pantalla la matriz resultante ?
    5.Volver hacia atrás.

'''
#------------
import os
#Para borrar pantalla, no funciona en Thonny.
def borrar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

#------------

def validar_opcion(opciones_minimas: int, opciones_maximas: int) -> str:
    '''
    Pre:Recibe dos números enteros que simbolizan la cantidad de opciones posibles.
    Post: Retorna un número entero dentro del rango de opciones.
    '''
    opcion = input("Ingrese una opción: ")
    while not opcion.isnumeric() or int(opcion) > opciones_maximas or int(opcion) < opciones_minimas:
        print("La opción ingresada, no es valida")
        opcion = input("Intente nuevamente, ingrese su opción: ")
    return opcion

def validar_numero() -> int:
    '''
    Pre: ~
    Post: Retorna un número entero valido
    '''
    numero = input("Ingrese el tamaño de la matriz: ")
    while not numero.isnumeric():
        print("Lo que ingresó no fue un número, intente nuevamente")
        numero = input("Ingrese el tamaño de la matriz")

    return int(numero)

def mostrar_matriz(matriz: list, tam_matriz: int) -> None:
    '''
    Pre: Recibe una matriz y su tamaño
    Post: Muestra en pantalla la matriz pasada por parámetro
    '''
    for i in range(tam_matriz):
        for j in range(tam_matriz):
            print(matriz[i][j], end=",")
        print("\n")

def mostrar_matrices(matriz_a: list, matriz_b:list, tam_matriz:int) -> None:
    '''
    Pre: Recibe las matrices A y B, y su tamaño.
    Post: Muestra en pantalla las matrices A y B.
    '''
    print("----Matriz A----")
    mostrar_matriz(matriz_a, tam_matriz)
    print("----Matriz B----")
    mostrar_matriz(matriz_b, tam_matriz)

def multiplicar_matrices(matriz_a: list, matriz_b:list, tam_matriz: int) -> None: #A completar
    '''
    Pre: Recibe las matrices A y B previamente generadas, y su tamaño.
    Post: Multiplica las matrices pasadas por párametro y luego muestra en pantalla el resultado.
    '''
    pass

def mostrar_suma_de_matrices(matriz_a: list, matriz_b: list, tam_matriz: int) -> None: #A completar
    '''
    Pre: Recibe dos matrices A y B previamente generadas, y su tamaño.
    Post: Suma las dos matrices pasadas por parámetro y luego muestra en pantalla el resultado
    '''
    matriz_resultante = list()
    for i in range(tam_matriz):
        fila_resultante = list()
        for j in range(tam_matriz):
            Aij = matriz_a[i][j]
            Bij = matriz_b[i][j]
            fila_resultante.append(Aij+Bij)
        matriz_resultante.append(fila_resultante)
    
    mostrar_matriz(matriz_resultante, tam_matriz)
        
def modificar_matriz(matriz: list, tam_matriz:int) -> None: #A completar
    '''
    Pre: Recibe una matriz A previamente generada y su tamaño.
    Post: Modifica los elementos de la matriz pasada por parámetro.
    '''
    for i in range(tam_matriz):
        for j in range(tam_matriz):
            nuevo_elemento = validar_numero()
            matriz[i][j] = nuevo_elemento

def generar_matriz_identidad(tam_matriz: int) -> list: #A completar
    '''
    Pre: Recibe el tamaño deseado de la matriz a generar.
    Post: Retorna una matriz identidad de tamaño N.
    '''
    matriz_identidad = []

    for i in range(tam_matriz):
        fila = []
        for j in range(tam_matriz):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        matriz_identidad.append(fila)
    
    return matriz_identidad

def aplicar_operacion(opcion: str, matriz_a: list, matriz_b: list, tam_matriz: int) -> None:
    if opcion == '1':
        # modificar_matriz(matriz_a, tam_matriz)
        # modificar_matriz(matriz_b, tam_matriz)
        pass
    elif opcion == '2':
        mostrar_matrices(matriz_a, matriz_b, tam_matriz)
    elif opcion == '3':
        mostrar_suma_de_matrices(matriz_a, matriz_b, tam_matriz)
        pass
    elif opcion == '4':
        # multiplicar_matrices(matriz_a, matriz_b, tam_matriz)
        pass
    
def menu_de_operaciones(matriz_a: list, matriz_b: list, tam_matriz: int) -> None:
    '''
    Pre: Recibe dos matrices A y B previamente generadas, y su tamaño.
    Post: Si el usuario elige la opción 5, se vuelve hacia atras para generar nuevas matrices o cerrar el programa.
    Sino, se aplica la operación de matrices elegida por el usuario.
    '''
    volver_atras = False
    while not volver_atras:
        print("¿Qué operación desea realizar?")
        print("1.Modificar los elementos de A y B")
        print("2.Mostrar en pantalla las matrices actuales")
        print("3.Sumar A + B y mostrar en pantalla el resultado")
        print("4.Multiplicar A + B y mostrar en pantalla la matriz resultante")
        print("5.Volver hacia atrás")
        opcion = validar_opcion(1, 5)
        if opcion == '5':
            volver_atras = True
        else:
            aplicar_operacion(opcion, matriz_a, matriz_b, tam_matriz)
    #Si llegamos acá, volvimos hacia atras.

def menu_inicial():
    cerrar_programa = False
    while not cerrar_programa:
        print("Bienvenido a la Calculadora de matrices")
        print("Elija una opción: ")
        print("1.Crear dos matrices identidad A y B")
        print("2.Cerrar el programa")
        opcion = validar_opcion(1,2)
        if opcion == '2':
            cerrar_programa = True
        else:
            tam_matriz = validar_numero()
            matriz_a = generar_matriz_identidad(tam_matriz)
            matriz_b = generar_matriz_identidad(tam_matriz)
            menu_de_operaciones(matriz_a, matriz_b, tam_matriz)
    #Si llegamos acá, terminamos el programa.

def main() -> None:
    menu_inicial()
main()


















'''

    (A11 A12 A13)           (B11 B12 B13)
A = (A21 A22 A23)       B = (B21 B22 B23)
    (A31 A32 A33)           (B31 B32 B33)



        (A11+B11 A12+B12 A13+B13)
A + B = (A21+B21 A22+B22 A23+B23)
        (A31+B31 A32+B32 A33+B33)
    
    (1 0 0)
Ia =(0 1 0)
    (0 0 1)

'''