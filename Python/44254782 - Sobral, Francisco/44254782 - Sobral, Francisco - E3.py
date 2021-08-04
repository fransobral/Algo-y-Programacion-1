def cargar_disciplina(datos_olimpicos:dict)-> None:
    disciplina = input("Por favor ingrese la disciplina que desea cargar: ")

    for disciplinas in datos_olimpicos:
        while disciplina == disciplinas:
            disciplina = input("La disciplina que usted ingreso ya exsiste, por favor ingrese una nueva: ")

    oro = input("Por favor ingrese quien fue el ganador de la medalla de oro: ")
    plata = input("Por favor ingrese quien fue el ganador de la medalla de plata: ")
    bronce = input("Por favor ingrese quien fue el ganador de la medalla de bronce: ")
    record_mundial = input("Por favor ingrese si se rompio o no un record mundial (si/no): ")

    if record_mundial == "si" or record_mundial == "Si":
        record = 1
    else:
        record = 0

    datos_olimpicos[disciplina] = [oro,plata,bronce,record]

def separar_por_medallas(datos_olimpicos:dict)-> tuple:
    oro_list = list()
    plata_list = list()
    bronce_list = list()
    paises = list()

    for info in datos_olimpicos.values():
        oro_list.append(info[0])
        plata_list.append(info[1])
        bronce_list.append(info[2])
        if info[0] not in paises:
            paises.append(info[0])
        if info[1] not in paises:
            paises.append(info[1])
        if info[2] not in paises:
            paises.append(info[2])
    
    return paises,oro_list,plata_list,bronce_list

def crear_medallero(paises:list,oro_list:list,plata_list:list,bronce_list)-> list:
    medallero = list()
    
    for pais in paises:
        oro = 0
        plata  = 0
        bronce = 0

        for pais_oro in oro_list:
            if pais in pais_oro:
                oro += 1

        for pais_plata in plata_list:
            if pais in pais_plata:
                plata += 1

        for pais_bronce in bronce_list:
            if pais in pais_bronce:
                bronce += 1
        medallero.append([pais,oro,plata,bronce])
    return medallero

def medallero_olimpico(datos_olimpicos:dict)-> None:

    paises,oro_list,plata_list,bronce_list = separar_por_medallas(datos_olimpicos)
    medallero = crear_medallero(paises,oro_list,plata_list,bronce_list)

    medallero = sorted(medallero, key=lambda tup: (-tup[1],-tup[2],-tup[3]))

    for info in medallero:
        print(f"{info[0]} tiene {info[1]} de oro, {info[2]} de plata y {info[3]} de bronce.")
            
def records_mundiales(datos_olimpicos:dict)-> None:
    record_list = list()
    paises_con_records = list()
    paises_mas_ganadores = list()

    for info in datos_olimpicos.values():
        if info[3] == 1:
            record_list.append(info[0])
    for pais in record_list:
        cantidad = record_list.count(pais)
        if [pais,cantidad] not in paises_con_records:
            paises_con_records.append([pais,cantidad])

    pais, maximo= max(paises_con_records, key=lambda item: item[1])
    maximo_nuevo = maximo
    pais_nuevo = pais

    while maximo_nuevo == maximo:
        maximo = maximo_nuevo
        pais = pais_nuevo
        paises_mas_ganadores.append([pais,maximo])
        index_pais_ganador = paises_con_records.index([pais,maximo])
        paises_con_records.pop(index_pais_ganador)
        if len(paises_con_records) > 0:
            pais_nuevo, maximo_nuevo = max(paises_con_records, key=lambda item: item[1])
        else:
            maximo_nuevo = 0

    if len(paises_mas_ganadores) > 1:
        print(f"Estos paises son los que mas records quebraron con un total de {paises_mas_ganadores[0][1]}:")    
        for info in paises_mas_ganadores:
            print(f"{info[0]}")
    else:
        print(f"\n{paises_mas_ganadores[0][0]} fue el pais que mas records rompio con {paises_mas_ganadores[0][1]} records.")

def obtener_medallas_totales(medallero:list)-> list:
    medallas_totales = list()

    for info in medallero:
        total_medallas = info[1] + info[2] + info [3]
        medallas_totales.append([info[0],total_medallas])

    medallas_totales.sort(reverse=True, key=lambda x: x[1])

    return medallas_totales

def top_5_podio(datos_olimpicos:dict)-> None:

    paises,oro_list,plata_list,bronce_list = separar_por_medallas(datos_olimpicos)
    medallero = crear_medallero(paises,oro_list,plata_list,bronce_list)
    medallas_totales = obtener_medallas_totales(medallero)

    for i in range(5):
        print(f"Nº{i+1}: {medallas_totales[i][0]} con {medallas_totales[i][1]} medallas.")

def porcentaje_medallas_pais(datos_olimpicos:dict)-> None:
    paises,oro_list,plata_list,bronce_list = separar_por_medallas(datos_olimpicos)
    medallero = crear_medallero(paises,oro_list,plata_list,bronce_list)
    medallas_totales_por_pais = obtener_medallas_totales(medallero)
    total_de_medallas = 0

    for info in medallas_totales_por_pais:
        total_de_medallas += info[1]

    for info in medallas_totales_por_pais: #no hay necesidad de ordenarlo devuelta ya que en la funcion obtener_medallas_totales ya las ordena.
        porcentaje = round(info[1]/total_de_medallas*100,2)
        print(f"{info[0]} gano un {porcentaje}% de las medallas este año.")

def menu(datos_olimpicos:dict)-> None:
    eleccion = "indiferente"
    while eleccion != "f":
        eleccion = input("""
        a) Cargar nueva disciplina.
        b) Crear medallero olimpico.
        c) Mostrar pais con mas records mundiales.
        d) Mostrar los 5 paises con mas podios.
        e) Mostrar porcentaje de medallas con respecto al total por pais.
        f) Salir del programa.
        Que opcion desea realizar?: """)

        if eleccion == "a":
            cargar_disciplina(datos_olimpicos)
        elif eleccion == "b":
            medallero_olimpico(datos_olimpicos)
        elif eleccion == "c":
            records_mundiales(datos_olimpicos)
        elif eleccion == "d":
            top_5_podio(datos_olimpicos)
        elif eleccion == "e":
            porcentaje_medallas_pais(datos_olimpicos)

def main()-> None:
    datos_olimpicos = {
    "Ciclismo de montaña":["GBR","SUI","ESP",0],
    "Sable individual femenino":["ROC","ROC","FRA",0],
    "Gimnasia por equipos masculino":["ROC","JPN","CHN",0],
    "Natacion 100m mariposa femenino":["CAN","CHN","AUS",1],
    "Natacion 100m libre masculino":["GBR","NED","ITA",1],
    "Triatlon":["NOR","GBR","NZL",0]}
    menu(datos_olimpicos)
    print("¡Muchas gracias por utilizar nuestro programa!")
main()
    
