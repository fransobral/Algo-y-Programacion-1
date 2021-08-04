
def ingreso_info_usuario(alumnos:dict) -> dict:
    alumno = dict()
    llave = 0
    año_ingreso = 0
    nombre = ""
    apellido = ""
    padron = 0
    carrera = ""
    cantidad_materias_aprobadas = 0
    nota_promedio = 0
    agregar_datos = True
    
    while agregar_datos:
        padron = int(input("Ingrese el padron del alumno: "))
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        carrera = input("Ingrese la carrera del alumno: ")
        cantidad_materias_aprobadas = int(input("Ingrese la cantidad de materias aprobadas del alumno: "))
        nota_promedio = float(input("Ingresa la nota promedio del alumno: "))
        año_ingreso = int(input("Ingrese el año de ingreso del alumno: "))

        corte = input("¿Quiere seguir ingresando datos <s/n>? ")
        if corte != "s":
            agregar_datos = False
        else:
            llave += 1
    
    alumno["padron"] = padron
    alumno["nombre"] = nombre
    alumno["apellido"] = apellido
    alumno["carrera"] = carrera
    alumno["cantidad_materias_aprobadas"] = cantidad_materias_aprobadas
    alumno["nota_promedio"] = nota_promedio
    alumno["año_ingreso"] = año_ingreso
    alumnos[llave] = alumno

    return alumnos

