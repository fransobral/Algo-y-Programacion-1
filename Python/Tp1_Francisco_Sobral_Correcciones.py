from random import randint,shuffle

def elegir_tablero() -> int:
    """
    Pre: Nada
    Post: Le pide al usuario que eliga el tamaño del tablero a utilizar.
    """
    eleccion_tablero = int(input("\n\nEstamos por comenzar, por favor eliga que tablero desea utilizar: 1) 4x4, 2) 8x8 o 3) 12x12 (1/2/3): "))
    if eleccion_tablero == 1:
        print("\nGenial! Usted a escogido el tablero de 4x4.\n")
        tam_matriz = 4 
    if eleccion_tablero == 2:
        print("\nGenial! Usted a escogido el tablero de 8x8.\n")
        tam_matriz = 8
    if eleccion_tablero == 3:
        print("\nGenial! Usted a escogido el tablero de 12x12.\n")
        tam_matriz = 12

    return tam_matriz

def almacenar_cantidad_cartas(dado:int,cartas:dict,configuracion_probabilidades:dict) -> dict:
    """ 
    Pre: Tengo el numero del dado y los rangos de probabilidad de cada carta.
    Post: Veo si tengo que sumar o no alguna carta comodin al jugador, y devuelve el valor obtenido de dichas cartas.
    """
    if dado > 0 and dado <= configuracion_probabilidades['Replay']:
        cartas['Replay'] += 1
    elif dado > configuracion_probabilidades['Replay'] and dado <= (configuracion_probabilidades['Replay'] + configuracion_probabilidades['Fatality']):
        cartas['Fatality'] += 1 #trasponer
    elif dado > (configuracion_probabilidades['Replay'] + configuracion_probabilidades['Fatality']) and dado <= (configuracion_probabilidades['Replay'] + configuracion_probabilidades['Fatality'] + configuracion_probabilidades['Layout']):
        cartas['Layout'] += 1 #mezcla todas las fichas del tablero del jugador que tiene la carta
    elif dado > (configuracion_probabilidades['Replay'] + configuracion_probabilidades['Fatality'] + configuracion_probabilidades['Layout']) and dado <= (configuracion_probabilidades['Total']):
        cartas['Toti'] += 1 #espeja el tablero del jugador que tiene la carta

    return cartas

def establecer_probabilidades_cartas(configuracion_probabilidades:dict) -> tuple:
    """
    Pre: Le paso los nombres de las probabilidades para almacenarlas para despues.
    Post: Le informa al usuario como quedaron las probabilidades de las cartas.
    """
    if configuracion_probabilidades['Total'] != 0:
        juego_con_comodines = True
        print("\nExcelente, asi quedaron las probabilidades:\n")
        if configuracion_probabilidades['Replay'] > 0:
            print(f"Si el dado sale entre 1 y {configuracion_probabilidades['Replay']}, te sumara una carta replay.\n")
        else:
            print("\nNo habra carta replay.\n")
        if configuracion_probabilidades['Fatality'] != 0:
            print(f"Si sale entre {configuracion_probabilidades['Replay'] + 1} y {configuracion_probabilidades['Replay'] + configuracion_probabilidades['Fatality']} te suma una carta fatality. \n")
        else:
            print("No habra carta fatality.\n")
        if configuracion_probabilidades['Layout'] != 0:
            print(f"Entre {configuracion_probabilidades['Replay'] + configuracion_probabilidades['Fatality'] + 1} y {configuracion_probabilidades['Replay'] + configuracion_probabilidades['Fatality'] + configuracion_probabilidades['Layout']} te suma una carta layout.\n")
        else:
            print("No habra carta layout.\n")
        if configuracion_probabilidades['Toti'] != 0:
            print(f"Y si sale entre {configuracion_probabilidades['Replay'] + configuracion_probabilidades['Fatality'] + configuracion_probabilidades['Layout'] + 1} y {configuracion_probabilidades['Total']}, te suma una carta toti.")
        else:
            print("No habra carta toti.\n")
    else:
        juego_con_comodines = False
        print("\nOptaste por jugar sin comodines.\n")

    return configuracion_probabilidades,juego_con_comodines

def pedir_probabilidades_cartas() -> tuple: 
    """ 
    Pre: Nada
    Post: Pide al usuario que establezca la probabilidad de cada carta comodin.
    """
    print("Vamos a establecer las probabilidades de las cartas comodin!")
    print("\nLas cartas comodin son 4, la carta replay, la fatality, la layout y la toti.\nLa primera te permite tener otro turno tras fallar la pareja, la segunda transpone el tablero del oponente,\nla tercera, mezcla todo el tablero del rival y le borra las parejas obtenidas, y por ultimo, la toti espeja el tablero rival.")
    print("\n")
    probabilidad_replay = int(input(f"Que probabilidad de que salga la carta replay desea tener? (%): "))
    probabilidad_fatality = int(input(f"Que probabilidad de que salga la carta fatality desea tener? (%): "))
    probabilidad_layout = int(input(f"Que probabilidad de que salga la carta layout desea tener? (%): "))
    probabilidad_toti = int(input(f"Que probabilidad de que salga la carta toti desea tener? (%): "))
     
    probabilidad_total = probabilidad_replay + probabilidad_fatality + probabilidad_layout + probabilidad_toti

    while probabilidad_total > 100:
        print("\n")
        print("La suma de esos valores exceden del 100%. Por favor ingrese devuelta sus probabilidades.")
        print("\n")
        probabilidad_replay = int(input(f"Que probabilidad de que salga la carta replay desea tener? (%): "))
        probabilidad_fatality = int(input(f"Que probabilidad de que salga la carta fatality desea tener? (%): "))
        probabilidad_layout = int(input(f"Que probabilidad de que salga la carta layout desea tener? (%): "))
        probabilidad_toti = int(input(f"Que probabilidad de que salga la carta toti desea tener? (%): "))
        probabilidad_total = probabilidad_replay + probabilidad_fatality + probabilidad_layout + probabilidad_toti
    
    configuracion_probabilidades = {'Replay': probabilidad_replay, 'Fatality': probabilidad_fatality, 'Layout': probabilidad_layout, 'Toti': probabilidad_toti, 'Total':probabilidad_total}
    configuracion_probabilidades,juego_con_comodines = establecer_probabilidades_cartas(configuracion_probabilidades)
    
    return configuracion_probabilidades,juego_con_comodines

def llenar_matriz(t_matriz:int) -> list:
    """ 
    Pre: El usuario ya ingreso el tamaño de la matriz que se va a utilizar para llenarla aqui.
    Post: Crea la matriz con sus numeros a encontrar.
    """
    
    matriz = list()
    contador = 0

    for i in range(t_matriz):
        print("")
        matriz.append([0] * t_matriz)
    for i in range(t_matriz): #columnas
        for j in range(t_matriz): #filas
            matriz[i][j] = contador
            if j % 2 == 1:
                contador += 1
    matriz = mezclar_matriz(matriz)

    return matriz

def llenar_matriz_escondida(tablero_ppal:list,aciertos:list) -> list:
    """ 
    Pre: El usuario ya ingreso el tamaño de la matriz que se va a utilizar para llenarla aqui.
    Post: Crea la matriz escondida que es la copia de la matriz original pero dada vuelta (escondida) y le da un nombre. En caso de tener aciertos, los muestra.
    """
    tablero_escondido = list()
    for i in range(len(tablero_ppal)):
        print("")
        tablero_escondido.append(["*"] * (len(tablero_ppal)))
    for i in range(len(tablero_ppal)): #columnas
        for j in range(len(tablero_ppal)): #filas
            tablero_escondido[i][j] = "*"

    if len(aciertos) != 0: #muestra los aciertos en pantall. Se utiliza cuando se mezcla la matriz ppal.
        tablero_2 = crear_copia_independiente_tablero(tablero_ppal)
        for i in range(len(aciertos)):
            columna,fila = buscar_coordeanada(aciertos[i],tablero_2)
            tablero_escondido = dar_vuelta_ficha(tablero_ppal,tablero_escondido,columna,fila)
  
    return tablero_escondido

def mezclar_matriz(matriz:list) -> list:
    """ 
    Pre: Le ingreso una matriz.
    Post: Me mezcla los numeros.
    """
    for j in range(len(matriz)):
        shuffle(matriz[j])

    matriz = trasponer_matriz(matriz)
    
    for j in range(len(matriz)):
        shuffle(matriz[j])
  

    return matriz

def mostrar_matriz(matriz: list) -> list:
    '''
    Pre: Recibe una matriz.
    Post: Muestra en pantalla la matriz pasada por parámetro
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(matriz[i][j], end = ",")
        print("\n")
    return matriz

def trasponer_matriz(matriz:list) -> list:  
    """ 
    Pre: Le ingreso una matriz.
    Post: Transpone la matriz ingresada.
    """
    transpuesta = [0]*len(matriz[0]) 
    for i in range(len(matriz)): 
        transpuesta[i] = [0]*len(matriz) 
        for j in range(len(matriz[i])): 
            transpuesta[i][j] = matriz[j][i] 
    return transpuesta

def crear_copia_independiente_tablero(tablero:list) -> list:
    """
    Pre: Recibe el tablero original.
    Post: Crea una copia del mismo pero independiente para poder modificarlo mas adelante.
     """
    tablero2 = list()

    for i in range(len(tablero)):
        tablero2.append(list())
        tablero2[i] = tablero[i].copy()

    return tablero2

def buscar_coordeanada(aciertos:int,tablero2:list) -> tuple: 
    """ 
    Pre: Recibe el tablero principal y los aciertos.
    Post: Busca la coordenada de ese acierto en el tablero principal.
    """
    fila = 0
    columna = 0
    encontrado = False

    while not encontrado and fila < len(tablero2):
        if aciertos in tablero2[fila]:
            encontrado = True
            columna = tablero2[fila].index(aciertos)
            tablero2[fila][columna] = "*"
        else:
            fila += 1

    return columna,fila

def dar_vuelta_ficha(tablero:list,tablero_escondido:list,columna:int,fila:int) -> list:
    """ 
    Pre: Recibe el tablero principal, el escondido, y las coordenadas de una ficha.
    Post: Reemplaza el valor de tablero escondido con el de tablero en las coordenadas recibidas.
    """
    tablero_escondido[fila][columna] = tablero[fila][columna]
    
    return tablero_escondido

def buscar_en_matriz(matriz:list,buscar:str) -> bool:
    """ 
    Pre: Le ingreso una matriz y un elemento a buscar.
    Post: Me devuelve si encontro ese elemento o no.
    """
    encontrado = False
    contador = 0

    while not encontrado and contador < len(matriz):
        if buscar in matriz[contador]:
            encontrado = True
        else:
            contador += 1

    return encontrado

def aplicar_match_ficha(eleccion:list,inventario_jugador:list,scoreboard:list) -> tuple:
    """ 
    Pre: Le pide la eleccion de las cartas, los tableros y el puntaje historico.
    Post: Me devuelve el tablero actualizdo con las parejas que encontro el usuario y en caso de una victoria, imprime la tabla de puntajes historicos.
    """    
    tablero = inventario_jugador[1]
    tablero_escondido = inventario_jugador[2]
    aciertos = inventario_jugador[5]
    comprobar_si_no_gano = buscar_en_matriz(tablero_escondido,"*")


    tablero_escondido = dar_vuelta_ficha(tablero,tablero_escondido,eleccion[0],eleccion[1])
    tablero_escondido = dar_vuelta_ficha(tablero,tablero_escondido,eleccion[2],eleccion[3])
    aciertos.append(tablero[eleccion[1]][eleccion[0]])
    aciertos.append(tablero[eleccion[3]][eleccion[2]])

    comprobar_si_no_gano = buscar_en_matriz(tablero_escondido,"*")

    if comprobar_si_no_gano:
        print("\nMuy bien, encontraste una pareja! Tenes otro turno.\n")
        mostrar_matriz(tablero_escondido)
        print("\n")
        eleccion = eleccion_ficha(tablero)
        print("\n")   
    else:
        print(imprimir_victoria(inventario_jugador[0],scoreboard))

    return tablero_escondido,comprobar_si_no_gano,eleccion

def mostrar_vuelta_ficha(tablero:list,tablero_escondido:list,eleccion:list) -> list():
    """
    Pre: Recibe los tableros y la eleccion.
    Post: Me muestra en pantalla la eleccion del jugador y retorna el tablero escondido en su posicion original.
          Impide que si el jugador elige una ficha que ya estaba dada vuelta la vuelva a ocultar.
    """
    eleccion_col_1,eleccion_fila_1,eleccion_col_2,eleccion_fila_2 = eleccion
    cambio_1 = False
    cambio_2 = False

    if tablero_escondido[eleccion_fila_1][eleccion_col_1] == ("*"):
        cambio_1 = True
        tablero_escondido = dar_vuelta_ficha(tablero,tablero_escondido,eleccion_col_1,eleccion_fila_1)
    
    if tablero_escondido[eleccion_fila_2][eleccion_col_2] == ("*"):
        cambio_2 = True
        tablero_escondido = dar_vuelta_ficha(tablero,tablero_escondido,eleccion_col_2,eleccion_fila_2)

    mostrar_matriz(tablero_escondido)

    if cambio_1:
        tablero_escondido[eleccion_fila_1][eleccion_col_1] = ("*")
    if cambio_2:
        tablero_escondido[eleccion_fila_2][eleccion_col_2] = ("*")

    return tablero_escondido

def aplicar_no_mach(eleccion:list,inventario_jugador:list) -> list:
    """ 
    Pre: Le pide la eleccion de las cartas y los tableros.
    Post: Le muestra al jugador las cartas que escogio y las vuelve a dar vuelta.
    """
    comprobar_si_no_gano = buscar_en_matriz(inventario_jugador[2],"*")
    tablero = inventario_jugador[1]
    tablero_escondido = inventario_jugador[2]

    if comprobar_si_no_gano == False:    
        print("")
    else:
        print("")
        tablero_escondido = mostrar_vuelta_ficha(tablero,tablero_escondido,eleccion)

        print("\nEso no es una pareja! Asi quedo tu tablero!")
        print("\n")
        mostrar_matriz(tablero_escondido)
        print("\n")
    return tablero_escondido

def convertir_fichas_int(eleccion:list) -> int:
    """
    Pre: Recibe los str de lalista.
    Post: Los transforma a int.
    """
    eleccion[0] = int(eleccion[0]) 
    eleccion[1] = int(eleccion[1]) 
    eleccion[2] = int(eleccion[2]) 
    eleccion[3] = int(eleccion[3])

    return eleccion

def convertir_fichas_str(eleccion:list) -> str:
    """
    Pre: Recibe los int de la lista.
    Post: Los transforma a str.
    """
    eleccion[0] = str(eleccion[0]) 
    eleccion[1] = str(eleccion[1]) 
    eleccion[2] = str(eleccion[2]) 
    eleccion[3] = str(eleccion[3])

    return eleccion

def verificar_eleccion_ficha(inventario_jugador:list,scoreboard:list) -> list:
    """ 
    Pre: Ingreso el tablero principal, el escondido, el nombre del jugador y la tabla de puntajes historicos.
    Post: Agarra la eleccion y verifica si fue match o no llamando a sus respectivas funciones.
    """
    tablero = inventario_jugador[1]
    eleccion = eleccion_ficha(tablero)
    comprobar_si_no_gano = buscar_en_matriz(inventario_jugador[2],"*")

    
    while tablero[eleccion[1]][eleccion[0]] == tablero[eleccion[3]][eleccion[2]] and comprobar_si_no_gano != False:
        tablero_escondido,comprobar_si_no_gano,eleccion = aplicar_match_ficha(eleccion,inventario_jugador,scoreboard)
    else:
        tablero_escondido = aplicar_no_mach(eleccion,inventario_jugador)
    inventario_jugador[2] = tablero_escondido
            
    return inventario_jugador

def verificar_rango_ficha(eleccion:list,tam_matriz:int)-> int:
    """
    Pre: Recibe las elecciones de columna y fila de cada ficha.
    Post: Verifica si esa eleccion esta dentro del rango permitido.
    """
    eleccion = convertir_fichas_int(eleccion)

    while 0 > eleccion[0] or eleccion[0] > (tam_matriz-1):
        print(f"\nLa columna 1 es menor a 0 o mayor a {tam_matriz-1}, por favor ingresala nuevamente.\n")
        eleccion[0] = input("Por favor ingresa el numero de columna de la ficha 1: ")
        eleccion = validacion_numero_ficha_elegida(eleccion)
    while 0 > eleccion[1] or eleccion[1] > (tam_matriz-1):
        print(f"\nLa fila 1 es menor a 0 o mayor a {tam_matriz-1}, por favor ingresala nuevamente.\n")
        eleccion[1]= input("Por favor ingresa el numero de fila de la ficha 1: ")
        eleccion = validacion_numero_ficha_elegida(eleccion)
    while 0 > eleccion[2] or eleccion[2] > (tam_matriz-1):
        print(f"\nLa columna 2 es menor a 0 o mayor a {tam_matriz-1}, por favor ingresala nuevamente.\n")        
        eleccion[2] = input("Por favor ingresa el numero de columna de la ficha 2: ")
        eleccion = validacion_numero_ficha_elegida(eleccion)
    while 0 > eleccion[3] or eleccion[3] > (tam_matriz-1):   
        print(f"\nLa fila 2 es menor a 0 o mayor a {tam_matriz-1}, por favor ingresala nuevamente.\n")
        eleccion[3] = input("Por favor ingresa el numero de fila de la ficha 2: ")
        eleccion = validacion_numero_ficha_elegida(eleccion)

    return eleccion
    
def validacion_numero_elegido_igual(eleccion:list,tablero:list) -> int:
    """
    Pre: Recibe las elecciones de columna y fila de cada ficha.
    Post: Verifica si los numeros son iguales y devuelve unos que no lo sean.
    """
    tam_matriz = len(tablero)

    if (eleccion[0] == eleccion[2] and eleccion[1] == eleccion[3]):
        print("\nEsos numeros son iguales, intente nuevmente.")
        eleccion_ficha(tablero)
    else:
        verificar_rango_ficha(eleccion,tam_matriz)

    eleccion = convertir_fichas_int(eleccion)

    return eleccion

def validacion_numero_ficha_elegida(eleccion:list) -> int:
    """
    Pre: Recibe las elecciones de columna y fila de cada ficha.
    Post: Verifica si esa eleccion es un numero o no, y si lo es, lo convierte a int.
    """
    eleccion = convertir_fichas_str(eleccion)

    while not (eleccion[0].isnumeric()):
        print("\nLa columna 1 no es un numero, por favor ingresala nuevamente.\n")
        eleccion[0] = input("Por favor ingresa el numero de columna de la ficha 1 (empezando en cero): ")
    while not (eleccion[1].isnumeric()):
        print("\nLa fila 1 no es un numero, por favor ingresala nuevamente.\n")
        eleccion[1] = input("Por favor ingresa el numero de fila de la ficha 1 (empezando en cero): ")
    while not (eleccion[2].isnumeric()):
        print("\nLa columna 2 no es un numero, por favor ingresala nuevamente.\n")
        eleccion[2] = input("Por favor ingresa el numero de columna de la ficha 2 (empezando en cero): ")
    while not (eleccion[3].isnumeric()):
        print("\nLa fila 2 no es un numero, por favor ingresala nuevamente.\n")
        eleccion[3] = input("Por favor ingresa el numero de fila de la ficha 2 (empezando en cero): ")
    
    eleccion = convertir_fichas_int(eleccion)

    return eleccion

def eleccion_ficha(tablero:list) -> list:
    """ 
    Pre: ...
    Post: Le pide al usuario que eliga la eleccion de sus fichas a dar vuelta y devuelve dichos valores. 
    Si una esta fuera de rango o no es un numero, le pide que ingrese otra. 
    """
    print("\nRecorda que las filas y columnas arrancan en 0.\n")
    eleccion_col_1 = input("Por favor ingresa el numero de columna de la ficha 1: ")
    eleccion_fila_1 = input("Por favor ingresa el numero de fila de la ficha 1: ")
    eleccion_col_2 = input("Por favor ingresa el numero de columna de la ficha 2: ")
    eleccion_fila_2 = input("Por favor ingresa el numero de fila de la ficha 2: ")
    
    eleccion = [eleccion_col_1,eleccion_fila_1,eleccion_col_2,eleccion_fila_2]
    eleccion = validacion_numero_ficha_elegida(eleccion)
    eleccion = validacion_numero_elegido_igual(eleccion,tablero)

    return eleccion

def carta_replay()-> bool:
    """ 
    Pre: Le ingreso cuantas cartas tiene disponible, el tablero normal y escondido del oponente.
    Post: Le resto uno a la cantidad de cartas y asigno la variable replay_si que se utilizara mas adelante.
    """
    replay_si = True
    print("\nHas elegido utilizar la carta replay.\n")
    return replay_si

def carta_fatality(tablero_escondido_otro_jugador:list,tablero_otro_jugador:list)-> list:
    """ 
    Pre: Le ingreso cuantas cartas tiene disponible, el tablero normal y escondido del oponente.
    Post: Traspongo ambos tableros.
    """
    trasponer_matriz(tablero_escondido_otro_jugador)
    trasponer_matriz(tablero_otro_jugador)
    print("Has elegido utilizar la carta fatality.\n")
    
    return tablero_escondido_otro_jugador,tablero_otro_jugador

def carta_layout(tablero_otro_jugador:list,aciertos:list)-> list:
    """ 
    Pre: Le ingreso cuantas cartas tiene disponible, el tablero normal y escondido del oponente.
    Post: Mezclo el tablero principal y el escondido de igual manera y le resto uno a la cantidad de cartas.
    """
    tablero_otro_jugador = mezclar_matriz(tablero_otro_jugador)
    tablero_escondido_otro_jugador = llenar_matriz_escondida(tablero_otro_jugador,aciertos)
    print("Has elegido utilizar la carta layout.\n")
    
    return tablero_escondido_otro_jugador,tablero_otro_jugador

def carta_toti(tablero_escondido_otro_jugador:list,tablero_otro_jugador:list)-> list:
    """
    Pre: Le ingreso cuantas cartas tiene disponible, el tablero normal y escondido del oponente.
    Post: Espejo ambos tableros del rival y se me resta una carta toti.
    """
    tablero_otro_jugador = tablero_otro_jugador[::-1] #crea espejo
    tablero_escondido_otro_jugador = tablero_escondido_otro_jugador[::-1]
    print("Has elegido utilizar la carta toti.\n")

    return tablero_escondido_otro_jugador,tablero_otro_jugador

def utilizar_comodines(cartas:dict,inventario_oponente:list,replay_si:bool) -> tuple:
    """ 
    Pre: Ingreso las cartas y el inventario del oponente.
    Post: Aplico el comodin que haya elegido el usuario para la partida.
    """
    si_usar = "si"
    eleccion_carta = int(input(f"\nCual desea utilizar? 1)Replay, 2)Fatality, 3)Layout, 4)Toti: "))
    if eleccion_carta == 1:
        if cartas['Replay'] != 0:
            cartas['Replay'] -= 1
            replay_si = carta_replay()
            si_usar = "ya uso"
        else:
            print("\nNo tenes cartas de este comodin, por favor eliga otro.\n")
    elif eleccion_carta == 2:
        if cartas['Fatality'] != 0:
            cartas['Fatality'] -= 1
            inventario_oponente[2],inventario_oponente[1] = carta_fatality(inventario_oponente[2],inventario_oponente[1])
            si_usar = "ya uso"
        else:
            print("\nNo tenes cartas de este comodin, por favor eliga otro.\n")
    elif eleccion_carta == 3:
        if cartas['Layout'] != 0:
            cartas['Layout'] -= 1
            inventario_oponente[2],inventario_oponente[1] = carta_layout(inventario_oponente[1],inventario_oponente[5])
            si_usar = "ya uso"
        else:
            print("\nNo tenes cartas de este comodin, por favor eliga otro.\n")
    elif eleccion_carta == 4:
        if cartas['Toti'] != 0:
            cartas['Toti'] -= 1
            inventario_oponente[2],inventario_oponente[1] = carta_toti(inventario_oponente[2],inventario_oponente[1])
            si_usar = "ya uso"
        else:
            print("\nNo tenes cartas de este comodin, por favor eliga otro.\n")
    else:
        print("No elegiste ninguna carta valida.\n")

    return cartas,inventario_oponente,replay_si,si_usar

def comprobacion_de_comodines(inventario_jugador:list,inventario_oponente:list) -> tuple:
    """ 
    Pre: Ingreso los inventarios de los jugadores.
    Post: Me fijo si tiene comodines y le pregunta si los quiere usar.
    """
    replay_si = False
    cartas = inventario_jugador[3]
    if (cartas['Replay'] or cartas['Fatality'] or cartas['Layout'] or cartas['Toti'] != 0):
        print(f"{inventario_jugador[0]}, tienes {cartas['Replay']} replays, {cartas['Fatality']} fatalitys, {cartas['Layout']} layouts y {cartas['Toti']} cartas toti.\n")
        si_usar = input("Desea utilizar algun comodin? (si/no) ")
        while si_usar == "si":
            cartas,inventario_oponente,replay_si,si_usar = utilizar_comodines(cartas,inventario_oponente,replay_si)
        if si_usar != "si" and si_usar != "ya uso":
            print("\nElegiste no utilizar comodines.\n")
    else:
        print("No tenes ningun comodin.")

    return inventario_jugador,inventario_oponente,replay_si
       
def imprimir_victoria(jugador:int,scoreboard:list())-> list:
    """ 
    Pre: Ingreso el nombre del jugador y la tabla de puntajes.
    Post: Imprime mensaje de victoria con nombre personalizado y agrega el nombre a la tabla de puntajes historicos. 
    """
    print(f"Muy bien {jugador}, has ganado el juego!")
    print("\n")
    print("Tablero de partidas ganadas:\n")
    while len(scoreboard) > 3:
        scoreboard.pop(0) #elimina el elemento mas viejo
    
    scoreboard.append(f"Gano {jugador}.")

    return scoreboard
       
def orden_de_turno(inventario_jugador:list,inventario_oponente:list,configuracion_probabilidades:dict,juego_con_comodines:bool,scoreboard:list) -> list:
    """ 
    Pre: Ingreso los tableros, los nombres de los jugadores, las probabilidades, la cantidad de cartas comodin, si decide jugar con comodines o no y la tabla de puntajes.
    Post: Organiza el orden de las funciones del juego. 
    """
    comprobar_si_no_gano = inventario_jugador[4]

    if comprobar_si_no_gano: 
        print(f"Es turno de {inventario_jugador[0]}.\n")
        mostrar_matriz(inventario_jugador[2])

        if juego_con_comodines:
            dado = randint(1,100)
            print("\n")
            print(f"El dado salio en {dado}")
            print("\n")
            almacenar_cantidad_cartas(dado,inventario_jugador[3],configuracion_probabilidades)
            inventario_jugador,inventario_oponente,replay_si = comprobacion_de_comodines(inventario_jugador,inventario_oponente)
            
            if replay_si:
                inventario_jugador = verificar_eleccion_ficha(inventario_jugador,scoreboard)
                print("\nElegiste usar la carta replay, tenes otro turno!\n")
                inventario_jugador = verificar_eleccion_ficha(inventario_jugador,scoreboard)
            else:
                inventario_jugador = verificar_eleccion_ficha(inventario_jugador,scoreboard)
        else:
            inventario_jugador = verificar_eleccion_ficha(inventario_jugador,scoreboard)     
    else:
        print("")
    return inventario_jugador,inventario_oponente

def crear_tableros_jugadores(tam_matriz:int,aciertos:list) -> list:
    """ 
    Pre:Recibe el tamaño de la matriz y los aciertos (siempre vacios).
    Post: Crea los tableros del juego.
    """
    tablero = trasponer_matriz(llenar_matriz(tam_matriz))
    tablero_escondido = llenar_matriz_escondida(tablero,aciertos)

    return tablero,tablero_escondido

def menu(comenzar:str) -> None:
    """ 
    Pre: Recibe el string comenzar que define si se comienza el juego o no.
    Post: Es el encargado de comenzar el juego, crear las prioridades y elegir el tamaño de los tableros y permitirle al usuario volver a jugar otra partida.
    """
    print("Hola! Bienvenidos al memotest!")
    scoreboard = list()
    print("\n")
    while comenzar == "si":
        print("\n")
        configuracion_probabilidades,juego_con_comodines = pedir_probabilidades_cartas()
        tam_matriz = elegir_tablero()
        comenzar = division_de_jugadores(tam_matriz,configuracion_probabilidades,juego_con_comodines,scoreboard)
        if comenzar == "si":
            print("\nExcelente, comienza una nueva partida!\n")
        else:
            print("\nGracias por jugar al memotest!")

def crear_inventario_jugador(tam_matriz:int) -> list:
    """ 
    Pre: Recibe el tamaño de matriz y el nombre del jugador.
    Post: Crea ambos tableros, los aciertos las cartas y la comprobacion de victoria y las empaqueta en una lista.
    """
    nombre = input("Por favor ingrese su nombre: ")
    aciertos = list()
    tablero,tablero_escondido = crear_tableros_jugadores(tam_matriz,aciertos)
    cartas = {'Replay':0,'Fatality':0,'Layout':0,'Toti':0}
    comprobar_si_no_gano = buscar_en_matriz(tablero_escondido,"*")
    aciertos = list()
    inventario_jugador = [nombre,tablero,tablero_escondido,cartas,comprobar_si_no_gano,aciertos]
    return inventario_jugador

def division_de_jugadores(tam_matriz:int,configuracion_probabilidades:dict,juego_con_comodines:bool,scoreboard:list) -> str:
    """ 
    Pre: Me ingresa si el usuario decide comenzar la partida o no.
    Post: Divide las funciones entre jugador 1 y jugador 2. Ademas de esto, le permite al usuario jugar mas de una partida.
    """
    print("Empecemos con el jugador 1: ")
    inventario_jugador1 = crear_inventario_jugador(tam_matriz)
    print("Ahora el jugador 2!\n")
    inventario_jugador2 = crear_inventario_jugador(tam_matriz)
    comprobar_si_no_gano1 = inventario_jugador1[4]
    comprobar_si_no_gano2 = inventario_jugador2[4]

    while comprobar_si_no_gano1 and comprobar_si_no_gano2:
        orden_de_turno(inventario_jugador1,inventario_jugador2,configuracion_probabilidades,juego_con_comodines,scoreboard)
        comprobar_si_no_gano1 = buscar_en_matriz(inventario_jugador1[2],"*")
        
        if comprobar_si_no_gano1:
            orden_de_turno(inventario_jugador2,inventario_jugador1,configuracion_probabilidades,juego_con_comodines,scoreboard)            
            comprobar_si_no_gano2 = buscar_en_matriz(inventario_jugador2[2],"*")
        else: 
            print("")
    
    comenzar = input("\nDesea comenzar otra partida? (si/no): ")

    return comenzar

def main() -> None:
    comenzar = input("Desea comenzar la partida? (si/no): ")
    print("\n")
    if comenzar == "si":
        menu(comenzar)    
    else:
        print("No comenzaremos la partida, que tengas un buen dia!")

main()
