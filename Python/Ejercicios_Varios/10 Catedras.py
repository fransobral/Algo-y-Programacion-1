nombre = ""
apellido = ""
catedra = 0
ccat1 = 0
ccat2 = 0
ccat3 = 0
cat1 = 0
cat2 = 0
cat3 = 0
nota = 0
padron = 0
max1 = 0
max2 = 0
max3 = 0
minF = 0
prom1 = 0
prom2 = 0
prom3 = 0
prom = 0
alumnos = 0
maximo = 0
pad1 = 0
pad2 = 0
pad3 = 0
mcat = 0
minimo = 11
snota1 = 0
snota2 = 0
snota3 = 0
alumnost = int(ccat1 + ccat2 + ccat3)
promcat = int((prom1+prom2+prom3)/3)
comando = "si"

while comando != "no":
    catedra = int(input("Ingrese numero de catedra 1, 2 o 3: "))
    apellido = input("Apellido: ")
    nombre = input("Nombre: ")
    padron = input("Padrón: ")
    nota = int(input("Nota final: "))
    if nota > maximo:
        maximo = nota
    elif catedra == 1:
        ccat1 += 1
        snota1 += nota
        if maximo > max1:
            max1 = maximo
            pad1 = padron
        if prom1 > prom:
            prom == prom1
            mcat == catedra
        prom1 = int(snota1/ccat1)
    elif catedra == 2:
        ccat2 += 1
        snota2 += nota
        if maximo > max2:
            max2 = maximo
            pad2 = padron
        prom2 = int(snota2/ccat2)
        if prom2 > prom:
            prom == prom2
            mcat == catedra
    elif catedra == 3:
        ccat3 += 1
        snota3 += nota
        if maximo > max2:
            max2 = maximo
            pad3 = padron
        prom3 = int(snota3/ccat3)
        if prom3 > prom:
            prom == prom3
            mcat == catedra
    elif nota < minimo:
        minimo = nota

    

    comando = input("Desea agregar mas datos? (si/no) ")

print(f"La nota maxima de la catedra 1 fue : {max1} y el alumno fue {pad1}. Por otro lado, el promedio de la misma fue de {prom1}.")
print((f"La nota maxima de la catedra 2 fue : {max2} y el alumno fue {pad2}. Por otro lado, el promedio de la misma fue de {prom2}."))
print((f"La nota maxima de la catedra 2 fue : {max3} y el alumno fue {pad3}. Por otro lado, el promedio de la misma fue de {prom3}."))
print(f"La peor nota fue: {minimo} y el mayor promedio de catedra lo tuvo la catedra {mcat} con un promedio de {prom}.")
print(f"La cantidad de alumnos totales fue de {alumnost}")


    



