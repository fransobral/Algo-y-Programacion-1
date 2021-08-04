
'''
"@RumboCircular" es un emprendimiento que enseña a cuidar el medioambiente. Rumbo Circular además
de dictar cursos de capacitación sobre medioambiente en empresas, lanzó un conjunto de cursos para la comunidad
general.
Estos cursos son los siguientes:
- Aprendé a hacer tu propio compost (1 día de curso). Costo $950
- Los niños y el medioambiente (para padres e hijes) (2 días de curso). Costo $990
- Tu huerta orgánica (4 días de curso). Costo $2500
El gran éxito de de estos cursos hizo que RumboCircular nos consultara para que los asesoremos para la creación de
un pequeño sistema que permita organizar la asistencia de los participantes.
Los requerimientos que nos solicitan son los siguientes:
a- Crear un menú que permita el acceso a los siguientes puntos.
b- Modificación de cursos. Se podrá modificar la siguiente infomación de los cursos. Nombre, cantidad de días,
costo.
c- Listar todos los cursos cuyo costo sea superior a 1150 pesos.
d- Cargado de asistentes a los cursos definidos.
e- Mostrar el listado de todos los cursos y sus respectivos asistentes. Ordenados por nombre de curso en forma
ascendente.
'''

def modificacion_cursos(cursos:dict):
    curso = int(input("""
        Que curso desea modificar?
        1 - Compost
        2 - Niños
        3 - Huerta 
        """))
    
    eleccion = input("""
    a)Nombre
    b)Cantidad de dias
    c)Costo
    Que desea modificar?""")

    if eleccion == "a":
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        cursos[curso]["nombre"] = nuevo_nombre
    elif eleccion == "b":
        dias = int(input("Ingrese la cantidad de dias: "))
        cursos[curso]["cantidad_de_dias"] = dias
    elif eleccion == "c":
        precio = int(input("Ingrese el nuevo precio: "))
        cursos[curso]["costo"] = precio

def listar_cursos(cursos:dict):
    cursos_lista = list()

    for valor in cursos.values():
        if valor["costo"] > 1150:
            nombre = valor["nombre"]
            costo = int(valor["costo"])
            cursos_lista.append([nombre,costo])
    
    for curso in cursos_lista:
        print(f"{curso[0]} - ${curso[1]}")

def cargar_asistentes(cursos:dict):
    curso = int(input("""
        Que curso desea modificar?
        1 - Compost
        2 - Niños
        3 - Huerta 
        """))
    asistente = input("Ingrese el nombre del nuevo asistente: ")
    cursos[curso]["asistentes"].append(asistente)
    
def listar_cursos_asistentes(cursos:dict):
    cursos_lista = list()

    for valor in cursos.values():

        nombre = valor["nombre"]
        asistentes =valor["asistentes"]
        cursos_lista.append([nombre,asistentes])
    
    cursos_lista.sort(reverse=True, key=lambda x: x[0])

    for curso in cursos_lista:
        print(f"{curso[0]} - {curso[1]}")

def main() -> None:
    cursos = {
        1: {
            "nombre": "Aprendé a hacer tu propio compost",
            "costo": 950.0,
            "cantidad_de_dias": 1,
            "asistentes":["fran"]
        },
        2: {
            "nombre": "Los niños y el medioambiente",
            "costo": 990.0,
            "cantidad_de_dias": 2,
            "asistentes":["juan"]
        },
        3: {
            "nombre": "Tu huerta orgánica",
            "costo": 2500.0,
            "cantidad_de_dias": 4,
            "asistentes":["matias"]
        }    
    }

    eleccion = input("""
        a)Modificacion de cursos.
        b)Listar costos cuyo costo sea superior a $1150.
        c)Cargar asistentes a cursos definidos.
        d)Mostrar listado de cursos y sus asistentes.

        Cual de estas acciones desea realizar?: """)

    if eleccion == "a":
        modificacion_cursos(cursos)
    elif eleccion == "b":
        listar_cursos(cursos)
    elif eleccion == "c":
        cargar_asistentes(cursos)
    elif eleccion == "d":
        listar_cursos_asistentes(cursos)
        
main()