import os,csv

def calcular_promedio_sector(sector:list):
    total = 0
    
    for tupla in sector:
        total += tupla[3]
    promedio = total/len(sector)

    return promedio

def crear_lista_ordenada(archivo:str):
    lista_ordenada = list()

    with open(archivo,"r") as archivo:
        for linea in archivo:
            linea_separada = linea.split(";")
            lista_ordenada.append([linea_separada[0],int(linea_separada[1]),linea_separada[2],int(linea_separada[3])])
    return lista_ordenada
    
def listas_por_sector(lista:list):
    norte = list()
    este = list()
    sur = list()
    oeste = list()
    
    for tupla in lista:
        if tupla[0] == "Norte":
            norte.append(tupla)
        elif tupla[0] == "Sur":
            sur.append(tupla)
        elif tupla[0] == "Oeste":
            oeste.append(tupla)
        elif tupla[0] == "Este":
            este.append(tupla)

    return norte,este,oeste,sur

def promedio_temp_sector(norte,este,oeste,sur):

    print(f"Norte: {calcular_promedio_sector(norte)}")
    print(f"Sur: {calcular_promedio_sector(sur)}")
    print(f"Este: {calcular_promedio_sector(este)}")
    print(f"Oeste: {calcular_promedio_sector(oeste)}")

def mayor_menor_temp(norte,este,oeste,sur):

    promedios = list()

    prom_norte = calcular_promedio_sector(norte)
    prom_sur = calcular_promedio_sector(sur)
    prom_este = calcular_promedio_sector(este)
    prom_oeste = calcular_promedio_sector(oeste)

    promedios = [prom_norte,prom_sur,prom_este,prom_oeste]
    print(f"Max: {max(promedios)}")
    print(f"Min: {min(promedios)}")
    
def calcular_hora_temp(norte,este,oeste,sur):
    norte.sort(reverse=True, key=lambda x: x[3])
    este.sort(reverse=True, key=lambda x: x[3])
    oeste.sort(reverse=True, key=lambda x: x[3])
    sur.sort(reverse=True, key=lambda x: x[3])

    print(f"Max N: {norte[0][2]}, Min:{norte[-1][2]}")
    print(f"Max S: {sur[0][2]}, Min:{sur[-1][2]}")
    print(f"Max O: {oeste[0][2]}, Min:{oeste[-1][2]}")
    print(f"Max E: {este[0][2]}, Min:{este[-1][2]}")    

def crear_archivo_seguridad(lista_ordenada:list):
    try:
        with open("seguridad.csv", 'w') as seguridad:
            for tupla in lista_ordenada:
                if tupla[3] > 395 or tupla[3] < 385:
                    texto = f"{tupla[0]};{tupla[1]};{tupla[2]};{tupla[3]}"
                    seguridad.write(f"{texto}\n")
        print("Archivo creado con exito.")
    except:
        print("Error creando el archivo.")
    
def cant_arreglos_pend(lista_ordenada:list):
    exsiste = os.path.exists('seguridad.csv')
    lineas_totales = 0

    if exsiste == False:
        crear_archivo_seguridad(lista_ordenada)

    with open("seguridad.csv") as seguridad:
        reader = csv.reader(seguridad)
        for linea in reader:
            lineas_totales +=1

        print(f"Usted tiene {lineas_totales} arreglos pendientes.")

def sector_problem(lista_ordenada):
    exsiste = os.path.exists('seguridad.csv')
    reader_separada = list()
    if exsiste == False:
        crear_archivo_seguridad(lista_ordenada)

    with open("seguridad.csv") as seguridad:
        reader = csv.reader(seguridad)
        data = list(tuple(rec) for rec in csv.reader(seguridad, delimiter=";")) #me pone el csv en un for mato legible de lista para dsps aplicar el for.
        for linea in data:
            reader_separada.append([linea[0],int(linea[1]),linea[2],int(linea[3])])

        norte,este,oeste,sur = listas_por_sector(reader_separada)

    listas_juntas = [("norte",len(norte)),("sur",len(sur)),("este",len(este)),("oeste",len(oeste))]
    listas_juntas.sort(reverse=True, key=lambda x: x[1])

    print(f"EL sector mas problematico fue el {listas_juntas[0][0]}.")

def main():
    print("""
    1) Informar el promedio de temperatura de cada sector.
    2) Determinar el sector con mayor temperatura y el sector con menor temperatura.
    3) Informar la hora de mayor y menor temperatura de cada sector.
    4) Crear el archivo de seguridad respetando el formato requerido.
    5) Informar cuantos tubos deben revisarse.
    6) Informar el sector mas problemático (mayor numero de tubos a revisarse).
    """)
    eleccion = int(input("Seleccione la opcion: "))

    lista_ordenada = crear_lista_ordenada("temperatura.txt")
    norte,este,oeste,sur = listas_por_sector(lista_ordenada)

    if eleccion == 1:
        promedio_temp_sector(norte,este,oeste,sur)
    elif eleccion == 2:
        mayor_menor_temp(norte,este,oeste,sur)
    elif eleccion == 3:
        calcular_hora_temp(norte,este,oeste,sur)
    elif eleccion == 4:
        crear_archivo_seguridad(lista_ordenada)
    elif eleccion == 5:
        cant_arreglos_pend(lista_ordenada)
    elif eleccion == 6:
        sector_problem(lista_ordenada)

main()

#next(csv_reader) #Evitamos leer el header