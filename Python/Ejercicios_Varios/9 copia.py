'''
Se pide hacer un programa que ingrese 8 juegos de n valores positivos cada uno.
Considerar un condiciòn de corte para el n.
Calculando el promedio de cada juego, el máximo de cada juego y el mínimo de todos los juegos.
'''
CANT_JUEGOS = 8
for juego in range(1, CANT_JUEGOS + 1):
    print(f"\n\nJuego {juego}")
    print("#####################")
    prom = 0
    suma = 0
    numero = int(input("Ingrese numero o -1 para salir: "))
    cantidad = 0
    max = numero
    if juego == 1: min = numero
    while numero != -1:
        if numero > max: max = numero
        if numero < min:
            min = numero
            min_juego = juego
        cantidad += 1
        suma += numero
        prom = suma/cantidad
        numero = int(input("Ingrese numero o -1 para salir: "))
    print(f"\n\nEl promedio del juego fué {prom}\nEl máximo del juego fué el {max}")
print(f"\n\n\nEl mínimo de todos los juegos fué el {min}, en el juego {min_juego}")