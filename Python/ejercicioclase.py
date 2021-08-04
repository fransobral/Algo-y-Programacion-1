def agregar_alumno(alumnos : dict, nombre : str, padron : int, nota : float) -> None:
    '''
    Agrega el alumno al diccionario alumnos
    '''
    alumnos[padron] = [nombre, nota]

def mostrar_aprobados(alumnos):
    '''
    Recibe un diccionario con los alumnos. Muestra en pantalla todos los alumnos con nota > 4
    '''
    print("Los alumnos aprobados son: ")
    for alumno, nota in alumnos.values():
        if nota > 4:
            print(alumno) 

def quitar_alumno(alumnos : dict, padron : int) -> None:
    '''
    Elmina el alumno del diccionario alumnos
    '''
    alumnos.pop(padron)
    
def main():
    alumnos = {1: ["a", 10], 2: ["b",2]}
    print("""
        1 - Agregar un alumno: debe solicitarse nombre, padrón y nota.
        2 - Consultar aprobados: debe mostrar los alumnos con nota mayor a 4.
        3 - Cantidad de alumnos totales y promedio general.
        4 - Quitar a un  alumno.
        5 - Salir
        """)
    opcion = int(input("Elige una opcion: "))
    while opcion != 5:
        if opcion == 1:
            #Pido al usuario los datos del alumno
            nombre = input("Nombre del alumno: ")
            padron = int(input("Padron del alumno: "))
            nota = float(input("Nota del alumno: "))
            agregar_alumno(alumnos, nombre, padron, nota)
            print("Alumno agregado con exito")
        if opcion == 2:
            mostrar_aprobados(alumnos)
        if opcion == 3:
            suma_notas = 0
            for _, nota in alumnos.values():
                suma_notas += nota
            print(f"Alumnos totales: {len(alumnos)}, promedio general: {suma_notas/len(alumnos)}")
        if opcion == 4:
            padron = int(input("Ingrese el padron del alumno que desea eliminar: "))
            quitar_alumno(alumnos, padron)
            print("Alumno quitado con éxito")
        opcion = int(input("Vuelva a ingresar una opcion: "))
    print("Saliendo...")
main()