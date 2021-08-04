from random import choice

def cajero() -> dict:
    billetes = [1000,500,200,100,50,20,10]
    valor = int(input("Por favor ingrese el monto a retirar: "))
    diccionario_final = {1000:0,500:0,200:0,100:0,50:0,20:0,10:0}

    for billete in billetes:  
        diccionario_final[billete] = valor // billete #// division entera, sin resto
        valor = valor % billete # % resto de la division

    return diccionario_final

baldosas = "R,G,N,R,R,N,R,R,R,B,R,N"

def caminito(baldosas:str):
    baldosas = baldosas.split(",")
    opciones = ("B","N","G")
    for i in range(len(baldosas)):
        if baldosas[i] == "R":
            baldosas[i] = choice(opciones)
        while baldosas[i] == baldosas[i-1]:
            baldosas[i] = choice(opciones)

    baldosas = ",".join(baldosas)


    return print(baldosas)

print(cajero())
caminito(baldosas)





