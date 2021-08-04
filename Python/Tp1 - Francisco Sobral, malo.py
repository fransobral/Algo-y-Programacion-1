from random import randint,shuffle,seed

def tirar_dado() -> int:
    """ 
    Pre: Nada
    Post: Me da un numero random entre el 1 y el 100.
    """
    return randint(1,100)

def elegir_tablero() -> int:
    """
    Pre: Nada
    Post: Le pide al usuario que eliga el tamaño del tablero a utilizar.
    """
    confirmacion = "no"

    while confirmacion == "no":
        eleccion_tablero = int(input("\n\nEstamos por comenzar, por favor eliga que tablero desea utilizar: 1) 4x4, 2) 8x8 o 3) 12x12 (1/2/3/4): "))
        print("")
        if eleccion_tablero == 1:
            confirmacion = input("Genial! Usted a escogido el tablero de 4x4. Desea confirmar su eleccion? (si/no): ")
            print("")
            tam_matriz = 4 
        if eleccion_tablero == 2:
            confirmacion = input("Genial! Usted a escogido el tablero de 8x8. Desea confirmar su eleccion? (si/no): ")
            print("")
            tam_matriz = 8
        if eleccion_tablero == 3:
            confirmacion = input("Genial! Usted a escogido el tablero de 12x12. Desea confirmar su eleccion? (si/no): ")
            print("")
            tam_matriz = 12
        else:
            print("El numero ingresado no es correcto, intente nuevamente.")
    return tam_matriz

def almacenar_cantidad_cartas(dado:int,cartas:dict,configuracion_probabilidades:dict) -> dict:
    """ 
    Pre: Tengo el numero del dado y los rangos de probabilidad de cada carta.
    Post: Veo si tengo que sumar o no alguna carta comodin al jugador, y devuelve el valor obtenido de dichas cartas.
    """
    probabilidad_replay = configuracion_probabilidades["Replay"]
    probabilidad_fatality = configuracion_probabilidades["Fatality"]
    probabilidad_layout = configuracion_probabilidades["Layout"]
    probabilidad_total = configuracion_probabilidades["Total"]
    replay,fatality,layout,toti = cartas["Replay"],cartas["Fatality"],cartas["Layout"],cartas["Toti"]

    if dado > 0 and dado <= probabilidad_replay:
        replay += 1
    elif dado > probabilidad_replay and dado <= (probabilidad_replay + probabilidad_fatality):
        fatality += 1 #trasponer
    elif dado > (probabilidad_replay + probabilidad_fatality) and dado <= (probabilidad_replay + probabilidad_fatality + probabilidad_layout):
        layout += 1 #mezcla todas las fichas del tablero del jugador que tiene la carta
    elif dado > (probabilidad_replay + probabilidad_fatality + probabilidad_layout) and dado <= (probabilidad_total):
        toti += 1 #espeja el tablero del jugador que tiene la carta
    cartas = {"Replay":replay,"Fatality":fatality,"Layout":layout,"Toti":toti}
    return cartas

def establecer_probabilidades_cartas() -> tuple: 
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
    else:
        if probabilidad_total != 0:
            juego_con_comodines = True
            print("\nExcelente, asi quedaron las probabilidades:\n")
            if probabilidad_replay > 0:
                print(f"Si el dado sale entre 1 y {probabilidad_replay}, te sumara una carta replay.\n")
            else:
                print("\nNo habra carta replay.\n")
            if probabilidad_fatality != 0:
                print(f"Si sale entre {probabilidad_replay + 1} y {probabilidad_replay + probabilidad_fatality} te suma una carta fatality. \n")
            else:
                print("No habra carta fatality.\n")
            if probabilidad_layout != 0:
                print(f"Entre {probabilidad_replay + probabilidad_fatality + 1} y {probabilidad_replay + probabilidad_fatality + probabilidad_layout} te suma una carta layout.\n")
            else:
                print("No habra carta layout.\n")
            if probabilidad_toti != 0:
                print(f"Y si sale entre {probabilidad_replay + probabilidad_fatality + probabilidad_layout + 1} y {probabilidad_total}, te suma una carta toti.")
            else:
                print("No habra carta toti.\n")
        else:
            juego_con_comodines = False
            print("\nOptaste por jugar sin comodines.\n")

    configuracion_probabilidades = {"Replay": probabilidad_replay, "Fatality": probabilidad_fatality, "Layout": probabilidad_layout, "Toti": probabilidad_toti, "Total":probabilidad_total}

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

def llenar_matriz_escondida(ta_matriz:int) -> list:
    """ 
    Pre: El usuario ya ingreso el tamaño de la matriz que se va a utilizar para llenarla aqui.
    Post: Crea la matriz escondida que es la copia de la matriz original pero dada vuelta (escondida) y le da un nombre.
    """
    tablero = list()
    for i in range(ta_matriz):
        print("")
        tablero.append(["*"] * (ta_matriz))
    for i in range(ta_matriz): #columnas
        for j in range(ta_matriz): #filas
            tablero[i][j] = "*"

    return tablero

def mezclar_matriz(matriz1:list) -> list:
    """ 
    Pre: Le ingreso una matriz.
    Post: Me mezcla los numeros.
    """

    for i in range(len(matriz1)):
        for j in range(len(matriz1)):
            shuffle(matriz1[j])  

    matriz1 = trasponer_matriz(matriz1)


    for i in range(len(matriz1)):
        for j in range(len(matriz1)):
            shuffle(matriz1[j]) 

    return matriz1

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

def mostrar_matrices(matriz1: list, matriz2:list,jug1:str,jug2:str) -> None:
    '''
    Pre: Recibe las matrices A y B, y su tamaño.
    Post: Muestra en pantalla las matrices A y B.
    '''

    print(f"Tablero de {jug1}")
    print("")
    mostrar_matriz(matriz1)
    print(f"Tablero de {jug2}")
    print("")
    mostrar_matriz(matriz2)

def trasponer_matriz(matriz:list) -> list:  
    """ 
    Pre: Le ingreso una matriz.
    Post: Transpone la matriz ingresada.
    """
    matriz1 = list()

    for i in range(len(matriz)):
        print("")
        matriz1.append([0] * len(matriz))
    for i in range(len(matriz)): #columnas
        for j in range(len(matriz)): #filas
            matriz1[i][j] = matriz [j][i]
    return matriz1

def buscar_en_matriz(matriz:list,buscar:str) -> bool:
    """ 
    Pre: Le ingreso una matriz y un elemento a buscar.
    Post: Me devuelve si encontro ese elemento o no.
    """
    elemento = False

    for fila in matriz:
        if buscar in fila:
            elemento = True
        elif elemento == False: 
            for columna in matriz:
                if buscar in columna:
                    elemento = True
    return elemento

def verificar_match_ficha(tablero:list,tablero_escondido:list,jugador:str,scoreboard:list) -> tuple:
    """ 
    Pre: Ingreso el tablero principal, el escondido, el nombre del jugador y la tabla de puntajes historicos.
    Post: Me devuelve el tablero actualizdo con las parejas que encontro el usuario y en caso de una victoria, imprime la tabla de puntajes historicos.
    """
    comprobacion_victoria = buscar_en_matriz(tablero_escondido,"*")
    tam_matriz = len(tablero)
    eleccioncol1,eleccionfila1,eleccioncol2,eleccionfila2 = eleccion_ficha(tam_matriz)

    while tablero[eleccionfila1][eleccioncol1] == tablero[eleccionfila2][eleccioncol2] and comprobacion_victoria == True:
        tablero_escondido[eleccionfila1][eleccioncol1] = tablero[eleccionfila1][eleccioncol1]
        tablero_escondido[eleccionfila2][eleccioncol2] = tablero[eleccionfila2][eleccioncol2]

        comprobacion_victoria = buscar_en_matriz(tablero_escondido,"*")

        if comprobacion_victoria == True:
            print("\nMuy bien, encontraste una pareja! Tenes otro turno.")
            mostrar_matriz(tablero_escondido)
            print("\n")
            eleccioncol1,eleccionfila1,eleccioncol2,eleccionfila2 = eleccion_ficha(tam_matriz)
            print("\n")   
        else:
            print(imprimir_victoria(jugador,scoreboard))
    
    if comprobacion_victoria == False:    
        print("")
    else:
        print("\nEso no es una pareja! Asi quedo tu tablero!")
        print("\n")
        mostrar_matriz(tablero_escondido)
        print("\n")
            
    return tablero,tablero_escondido,comprobacion_victoria

def eleccion_ficha(tam_matriz:int) -> int:
    """ 
    Pre: Tengo el tamaño de la matriz para saber cuando se excede del rango de eleccion.
    Post: Le pide al usuario que eliga la eleccion de sus fichas a dar vuelta y devuelve dichos valores. Si una esta fuera de rango, le pide que ingrese otra. 
    """
    print("\nRecorda que las filas y columnas arrancan en 0.\n")
    eleccioncol1 = input("Por favor ingresa el numero de columna de la ficha 1: ")
    eleccionfila1= input("Por favor ingresa el numero de fila de la ficha 1: ")
    eleccioncol2 = input("Por favor ingresa el numero de columna de la ficha 2: ")
    eleccionfila2 = input("Por favor ingresa el numero de fila de la ficha 2: ")
    
    while not eleccioncol1.isnumeric() or not eleccionfila1.isnumeric() or not eleccioncol2.isnumeric() or not eleccionfila2.isnumeric():
        print("\nUno de los valores ingresados no es un numero, por favor ingreselos nuevamente.\n")
        eleccioncol1 = input("Por favor ingresa el numero de columna de la ficha 1 (empezando en cero): ")
        eleccionfila1= input("Por favor ingresa el numero de fila de la ficha 1 (empezando en cero): ")
        eleccioncol2 = input("Por favor ingresa el numero de columna de la ficha 2 (empezando en cero): ")
        eleccionfila2 = input("Por favor ingresa el numero de fila de la ficha 2 (empezando en cero): ")

    eleccioncol1 = int(eleccioncol1) 
    eleccionfila1 = int(eleccionfila1) 
    eleccioncol2 = int(eleccioncol2) 
    eleccionfila2 = int(eleccionfila2) 

    while 0 > eleccioncol1 or eleccioncol1 > (tam_matriz-1) or 0 > eleccionfila1 or eleccionfila1 > (tam_matriz-1) or 0 > eleccioncol2 or eleccioncol2 > (tam_matriz-1) or 0 > eleccionfila2 or eleccionfila2 > (tam_matriz-1) or (eleccioncol1 == eleccioncol2 and eleccionfila1 == eleccionfila2): 
        print(f"\nUno de los valores ingresados es menor a 0 o mayor a {tam_matriz-1} o ingreo la misma ficha dos veces, por favor ingreselos nuevamente.\n")
        eleccioncol1 = input("Por favor ingresa el numero de columna de la ficha 1: ")
        eleccionfila1= input("Por favor ingresa el numero de fila de la ficha 1: ")
        eleccioncol2 = input("Por favor ingresa el numero de columna de la ficha 2: ")
        eleccionfila2 = input("Por favor ingresa el numero de fila de la ficha 2: ")
        eleccioncol1 = int(eleccioncol1) 
        eleccionfila1 = int(eleccionfila1) 
        eleccioncol2 = int(eleccioncol2) 
        eleccionfila2 = int(eleccionfila2) 
    
    return eleccioncol1,eleccionfila1,eleccioncol2,eleccionfila2

def carta_replay(replay:int)-> tuple:
    """ 
    Pre: Le ingreso cuantas cartas tiene disponible, el tablero normal y escondido del oponente.
    Post: Le resto uno a la cantidad de cartas y asigno la variable replay_si que se utilizara mas adelante.
    """
    replay -= 1
    replay_si = True
    si_usar = "no"
    print("\nHas elegido utilizar la carta replay.\n")
    return replay,replay_si,si_usar

def carta_fatality(fatality:int,tablero_escondido_otro_jugador:list,tablero_otro_jugador:list)-> tuple:
    """ 
    Pre: Le ingreso cuantas cartas tiene disponible, el tablero normal y escondido del oponente.
    Post: Traspongo ambos tableros y le resto uno a la cantidad de cartas.
    """
    fatality -= 1
    tablero_escondido_otro_jugador = trasponer_matriz(tablero_escondido_otro_jugador)
    tablero_otro_jugador = trasponer_matriz(tablero_otro_jugador)
    si_usar = "no"
    print("Has elegido utilizar la carta fatality.\n")
    
    return fatality,tablero_escondido_otro_jugador,tablero_otro_jugador,si_usar

def carta_layout(layout:int,tablero_escondido_otro_jugador:list,tablero_otro_jugador:list)-> tuple:
    """ 
    Pre: Le ingreso cuantas cartas tiene disponible, el tablero normal y escondido del oponente.
    Post: Mezclo el tablero principal, vuelve el tablero escondido a cero y le resto uno a la cantidad de cartas.
    """
    layout -= 1
    tablero_otro_jugador = mezclar_matriz(tablero_otro_jugador)
    tablero_escondido_otro_jugador = llenar_matriz_escondida(len(tablero_otro_jugador))
    si_usar = "no"
    print("Has elegido utilizar la carta layout.\n")
    
    return layout,tablero_escondido_otro_jugador,tablero_otro_jugador,si_usar

def carta_toti(toti:int,tablero_escondido_otro_jugador:list,tablero_otro_jugador:list)-> tuple:
    toti -= 1
    tablero_otro_jugador = tablero_otro_jugador[::-1] #crea espejo
    tablero_escondido_otro_jugador = tablero_escondido_otro_jugador[::-1]
    si_usar = "no"
    print("Has elegido utilizar la carta toti.\n")

    return toti,tablero_escondido_otro_jugador,tablero_otro_jugador,si_usar

def comprobacion_de_comodines(cartas:dict,jug_que_comienza:str,tablero_otro_jugador:list,tablero_escondido_otro_jugador:list) -> tuple:
    """ 
    Pre: Ingreso las cartas, el tablero del oponente y el nombre del jugador del turno.
    Post: Aplico el comodin que haya elegido el usuario para la partida.
    """
    replay_si = False
    si_usar = "si"
    replay,fatality,layout,toti = cartas["Replay"],cartas["Fatality"],cartas["Layout"],cartas["Toti"]

    while (replay or fatality or layout or toti != 0) and si_usar == "si" :
        print(f"{jug_que_comienza}, tienes {replay} replays, {fatality} fatalitys, {layout} layouts y {toti} cartas toti.\n")
        si_usar = input("Desea utilizar algun comodin? (si/no) ")
        if si_usar == "si":
            eleccion_carta = int(input(f"\nCual desea utilizar? 1)Replay, 2)Fatality, 3)Layout, 4)Toti: "))
            if eleccion_carta == 1:
                if replay != 0:
                    replay,replay_si,si_usar = carta_replay(replay)
                else:
                    print("\nNo tenes cartas de este comodin, por favor eliga otro.\n")
            elif eleccion_carta == 2:
                if fatality != 0:
                    fatality,tablero_escondido_otro_jugador,tablero_otro_jugador,si_usar = carta_fatality(fatality,tablero_escondido_otro_jugador,tablero_otro_jugador)
                else:
                    print("\nNo tenes cartas de este comodin, por favor eliga otro.\n")
            elif eleccion_carta == 3:
                if layout != 0:
                    layout,tablero_escondido_otro_jugador,tablero_otro_jugador,si_usar = carta_layout(layout,tablero_escondido_otro_jugador,tablero_otro_jugador)
                else:
                    print("\nNo tenes cartas de este comodin, por favor eliga otro.\n")
            elif eleccion_carta == 4:
                if toti != 0:
                    toti,tablero_escondido_otro_jugador,tablero_otro_jugador,si_usar = carta_toti(toti,tablero_escondido_otro_jugador,tablero_otro_jugador)
                else:
                    print("\nNo tenes cartas de este comodin, por favor eliga otro.\n")
            else:
                print("No elegiste ninguna carta valida.\n")
        else:
            print("\nElegiste no utilizar comodines.\n")
    else:
        print("")
    cartas = {"Replay":replay,"Fatality":fatality,"Layout":layout,"Toti":toti}

    return tablero_otro_jugador,tablero_escondido_otro_jugador,cartas,replay_si

def utilizacion_replay(tablero:list,tablero_escondido:list,replay_si:bool,jugador:str,scoreboard:list) -> tuple:
    """ 
    Pre: Le ingreso un tablero y uno escondido y veo si tiene otro turno gracias a la carta replay.
    Post: En caso de utilizar la carta replay, le dara otro turno al jugador. Sino simplemente jugara una ronda.
    """

    print("\n")

    while replay_si == True: #replay_si lo que hace es confirmar si el jugador opto por utilizar la carta replay o no.
        replay_si = False

        tablero,tablero_escondido,comprobacion_victoria = verificar_match_ficha(tablero,tablero_escondido,jugador,scoreboard)  
        print("Elegiste usar la carta replay, con lo cual tenes otro truno!")
        print("\n")
            
    tablero,tablero_escondido,comprobacion_victoria = verificar_match_ficha(tablero,tablero_escondido,jugador,scoreboard)    

    return tablero,tablero_escondido,replay_si,comprobacion_victoria
       
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
       
def orden_de_turno(jug:str,tablero:list,tablero_escondido:list,tablero_oponente:list,tablero_escondido_oponente:list,cartas:dict,configuracion_probabilidades:dict,juego_con_comodines:bool,scoreboard:list) -> tuple:
    """ 
    Pre: Ingreso los tableros, los nombres de los jugadores, las probabilidades, la cantidad de cartas comodin, si decide jugar con comodines o no y la tabla de puntajes.
    Post: Organiza el orden de las funciones del juego. 
    """
    comprobacion_victoria = buscar_en_matriz(tablero_escondido,"*")
    
    if comprobacion_victoria == True: 
        dado = tirar_dado()
        print(f"Es turno de {jug}.\n")
        mostrar_matriz(tablero_escondido)

        if juego_con_comodines == True:
            dado = tirar_dado()
            print("\n")
            print(f"El dado salio en {dado}")
            print("\n")
            cartas = almacenar_cantidad_cartas(dado,cartas,configuracion_probabilidades)
            tablero_oponente,tablero_escondido_oponente,cartas,replay_si = comprobacion_de_comodines(cartas,jug,tablero_oponente,tablero_escondido_oponente)
            tablero,tablero_escondido,replay_si,comprobacion_victoria = utilizacion_replay(tablero,tablero_escondido,replay_si,jug,scoreboard)
        else:
            tablero,tablero_escondido,comprobacion_victoria = verificar_match_ficha(tablero,tablero_escondido,jug,scoreboard)
            print("")
    else:
        print("")
    return tablero,tablero_escondido,tablero_oponente,tablero_escondido_oponente,cartas

def division_de_jugadores(comenzar:str) -> None:
    """ 
    Pre: Me ingresa si el usuario decide comenzar la partida o no.
    Post: Divide las funciones entre jugador 1 y jugador 2. Ademas de esto, le permite al usuario jugar mas de una partida.
    """
    cartas1 = {"Replay":0,"Fatality":0,"Layout":0,"Toti":0}
    cartas2 = {"Replay":0,"Fatality":0,"Layout":0,"Toti":0}
    print("Hola! Bienvenidos al memotest!")
    scoreboard = list()
    print("\n")
    while comenzar == "si":
        jugador_1 = input("Jugador 1, por favor ingrese su nombre: ")
        jugador_2 = input("Jugador 2, por favor ingrese su nombre: ")
        print("\n")
        configuracion_probabilidades,juego_con_comodines = establecer_probabilidades_cartas()
        tam_matriz = elegir_tablero()
        tablero_escondido1 = llenar_matriz_escondida(tam_matriz)
        tablero_escondido2 = llenar_matriz_escondida(tam_matriz)
        tablero1 = trasponer_matriz(llenar_matriz(tam_matriz))
        tablero2 = trasponer_matriz(llenar_matriz(tam_matriz))
        mostrar_matrices(tablero1,tablero2,jugador_1,jugador_2)

        comprobacion_victoria1 = buscar_en_matriz(tablero_escondido1,"*")
        comprobacion_victoria2 = buscar_en_matriz(tablero_escondido2,"*")

        while comprobacion_victoria1 == True and comprobacion_victoria2 == True:
            tablero1,tablero_escondido1,tablero2,tablero_escondido2,cartas1 = orden_de_turno(jugador_1,tablero1,tablero_escondido1,tablero2,tablero_escondido2,cartas1,configuracion_probabilidades,juego_con_comodines,scoreboard)
            comprobacion_victoria1 = buscar_en_matriz(tablero_escondido1,"*")
            
            if comprobacion_victoria1 == True:
                tablero2,tablero_escondido2,tablero1,tablero_escondido1,cartas2 = orden_de_turno(jugador_2,tablero2,tablero_escondido2,tablero1,tablero_escondido1,cartas2,configuracion_probabilidades,juego_con_comodines,scoreboard)
                comprobacion_victoria2 = buscar_en_matriz(tablero_escondido2,"*")
            else: 
                print("")
        
        comenzar = input("\nDesea comenzar otra partida? (si/no): ")
        if comenzar == "si":
            print("\nExcelente, comienza una nueva partida!\n")
        else:
            print("\nGracias por jugar al memotest!")

def main() -> None:
    comenzar = input("Desea comenzar la partida? (si/no): ")
    print("\n")
    if comenzar == "si":
        division_de_jugadores(comenzar)    
    else:
        print("No comenzaremos la partida, que tengas un buen dia!")

main()
