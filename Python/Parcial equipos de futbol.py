'''
Dada la siguiente estructura:
dicc_Equipos = {Equipo1: listaTítulos, "Equipo2": listaTítulos, …. "EquipoN":listaTítulos}
listaTítulos = [NombreTitulo, (dd,mm,aaaa), Jugador1, Jugador2, Jugador3… JugadorN]
Ejemplo:
Dicc_Equipos: {Boca: listaTitulos, River: listaTitulos, Racing: listaTítulos, SanLorenzo: listaTítulos….}
listaTítulos: [Libertadores, (12,08,2014), Sebastián Torrico, Julio Buffarini, Fabricio Fontanini, Santiago Gentiletti, Emmanuel Mas, Héctor Villalba, Juan Mercier, Néstor Ortigoza, Ignacio Piatti, Leandro Romagnoli, Mauro Matos, … JugadorN]
a- Hacer un ABM de la estructura. Los datos se piden al usuario por pantalla.
b- Hacer una función que reciba la estructura y un equipo de fútbol por parámetro
B1- Mostrar por pantalla el equipo que más títulos tiene
B2- Último título obtenido por el equipo pasado por parámetro en la función.
B3- El jugador con más títulos obtenidos del equipo pasado por parámetro.
'''
'''
equipos = {
    Boca : [
        [titulo1,anio,jugador],
        [titulo2,anio,jugador]
        ]
    }
'''
def ingresar_opcion():
    menu = [
        '1)Alta de equipo',
        '2)Baja',
        '3)Modificacion',
        '4)Mostrar el equipo que mas titulos tiene',
        '5)Mostrar el ultimo titulo obtenido por el equipo que elijas',
        '6)Mostrar el jugador con mas titulos obtenidos del equipo que elijas'
    ]
    for i in range(len(menu)):
        print(menu[i])
    opcion=input("Ingrese una opcion: ")
    while not (opcion.isnumeric() or int(opcion)< 0 or int(opcion)> 6):
        opcion= input("Debe ingresar otro valor para n que sea positivo: ")
    return int(opcion)
def alta_equipos(equipos):
    lista_titulos = list()
    nombre = input("Ingrese el nombre del equipo: ")
    if nombre not in equipos.keys():
        equipos[nombre] = []
    cant_titulos = False
    while not cant_titulos: 
        lista_titulo = list()
        titulo = input('Ingrese el titulo ganado: ')
        ##lista_titulo.append(titulo)
        fecha = input('Ingrese la fecha(dd,mm,aaaa): ')
        lista_titulo.append(fecha)
        cant_jugadores = False
        while not cant_jugadores: 
            jugador = input('Ingrese un jugador: ')
            lista_titulo.append(jugador)
            corte = input("Desea introducir otro jugador (s|n)? ")
            if corte != 's':
                cant_jugadores = True
        lista_titulos.append(lista_titulo)
        corte2 = input("Desea introducir otro titulo (s|n)? ")
        if corte2 != 's':
            cant_titulos = True
    equipos[nombre] = lista_titulos
    print(equipos)
    return equipos
def baja_equipos(equipos):
    for teams in equipos:
        print(f"{teams}")
    opcion = input("Cual equipo desea eliminar? ")
    del equipos[opcion]
    return equipos    
def modificacion_equipos(equipos):
    for teams in equipos:
        print(f"{teams}")
    opcion = input("Cual equipo desea modificar? ")
    print('\n')
    print(equipos[opcion])
    print(equipos[opcion][0])
    for i in range(len(equipos[opcion])):
        print(f'{i+1}{equipos[opcion][i]}')
    opcion2 = int(input('Cual lista quieres modificar? '))
    opcion2-=1
    for i in range(len(equipos[opcion][opcion2])):
        print(f'{i+1}) {equipos[opcion][opcion2][i]}')
    print('\n')
    entrada= int(input("Que valor desea modificar? "))
    entrada-=1
    print(f'Se eliminara el dato {equipos[opcion][opcion2][entrada]}')
    dato = input('Qu nuevo dato quieres ingresar por este: ')
    equipos[opcion][opcion2].pop(entrada)
    equipos[opcion][opcion2].insert(entrada, dato)
    print('\n')
    # if entrada == 0:
    #     torneo = input(f"Ingrese un nuevo Torneo ganado: ")
    #     equipos[opcion][entrada] = torneo
    # if entrada == 1:
    #     fecha = input(f"Ingrese una nueva fecha: ")
    #     equipos[opcion][entrada] = fecha
    # if entrada == 3:
    #     cant_fechas = False
    #     fechas = []
    #     while not cant_fechas:
    #         fecha = input(f"Ingrese una nueva {entrada}: ")
    #         fechas.append(fecha)
    #         corte = input("Desea introducir otra fecha (s|n)? ")
    #         if corte != 's':
    #             cant_fechas = True
    #     cursos[opcion][entrada] = fechas
    print(equipos)
    return equipos
def equipo_mas_ganador(equipos):
    equipo_ganador = ['',0] #[equipo mas ganador,cant de veces]
    for equipo,valor in equipos.items():
        if len(valor)> equipo_ganador[1]:
            equipo_ganador[0] = equipo
            equipo_ganador[1] = len(valor)
    print(f'El equipo mas ganador es {equipo_ganador[0]}, con {equipo_ganador[1]} titulos')
def utimo_titulo(equipos):
    ultimo_titu = ['',0]#[ultimo titulo,anio]
    for teams in equipos:
        print(f"{teams}")
    equipo = input('Elija un equipo de los siguientes posibles: ')
    for i in range(len(equipos[equipo])):
        if ultimo_titu[1] < equipos[equipo][i][1]:
            ultimo_titu[0] = equipos[equipo][i][0]
            ultimo_titu[1] = equipos[equipo][i][1]
    print(f'El ultimo torneo de {equipo} es {ultimo_titu[0]} en el anio {ultimo_titu[1]}')
def jugador_mas_titulos(equipos):
    jugadores = dict()    
    maximo_jugador=''   
    for teams in equipos:
        print(f"{teams}")
    equipo = input('Elija un equipo de los siguientes posibles: ')
    for i in range(len(equipos[equipo])):
        for j in range(2,len(equipos[equipo][i])):
            if equipos[equipo][i][j] not in jugadores.keys():
                jugadores[equipos[equipo][i][j]] = 1
            else:
                jugadores[equipos[equipo][i][j]] +=1
    maximo_jugador = max(jugadores, key=jugadores.get)
    print(f'El jugador con mas titulos es: {maximo_jugador}')
def main():
    equipos = dict()
    corte = False
    while not corte:
        opcion = ingresar_opcion()
        if opcion == 1:
            equipos = alta_equipos(equipos)
            print(equipos)
        if opcion == 2:
            equipos = baja_equipos(equipos)
        if opcion == 3:
            equipos = modificacion_equipos(equipos)
        if opcion == 4:
            equipos = {
                'boca':[['inercontinental',2003,'matias donnet'],['libertadores',2000,'tevez','riquelme','palermo'],['torneo local',2019,'tevez','riquelme']],
                'river':[['copa desenso',2012,'trezeguet','ponzio']],
                'independiente':[['libertadores',1987,'bochinni','gigliotti']],
                'racing':[['liga',2014,'milito','pillud']],
                'san lorenzo':[['libertadores',2014,'blandi','ortigoza']]
            }
            equipo_mas_ganador(equipos)
        if opcion == 5:
            # equipos = {
            #     'boca':[['inercontinental',2003,'matias donnet'],['libertadores',2000,'tevez','riquelme','palermo'],['torneo local',2019,'tevez','riquelme']],
            #     'river':[['copa desenso',2012,'trezeguet','ponzio']],
            #     'independiente':[['libertadores',1987,'bochinni','gigliotti']],
            #     'racing':[['liga',2014,'milito','pillud']],
            #     'san lorenzo':[['libertadores',2014,'blandi','ortigoza']]
            # }
            utimo_titulo(equipos)
        if opcion == 6:
            jugador_mas_titulos(equipos)
        opcion2 = input('Desea volver al menu? (s|n) ')
        if opcion2 != 's':
            corte = True
    pass
main()