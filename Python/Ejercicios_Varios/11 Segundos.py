"""
1. Escribir una función que permita calcular la duración en segundos de un intervalo dado en horas,
 minutos y segundos.
2. Usando la función del ejercicio anterior, escribir un programa que pida al usuario dos intervalos
 expresados en horas, minutos y segundos, sume sus duraciones, y muestre por pantalla la duración total en horas,
  minutos y segundos.
"""



hora = int(input(f"Ingrese la hora: "))
minu = int(input(f"Ingrese los minutos: "))
seg = int(input(f"Ingrese los segundos: "))


def duracion (hora:int,minu:int,seg:int)->int:
    resultado = (hora*3600 + minu*60 + seg)
    print(f"Eso seria un total de {resultado} segundos.")
    return duracion
duracion(hora,minu,seg)
