def conversor(horas, minutos, segundos) -> int:
    resultado = horas*3600 + minutos*60 + segundos
    return resultado
suma = 0
for i in range(2):
    hora = int(input("ingrese las horas de su intervalo: "))
    minuto = int(input("ingrese los minutos de su intervalo: "))
    segundo = int(input("ingrese los segundos de su intervalo: "))
    intervalo = conversor(hora, minuto, segundo)
    suma += intervalo
def inversor(segundos)-> int:
    horas = suma // 3600     # // me da el cociente y % da resto 
    minutos = (suma - horas*3600) // 60
    segundos = suma - horas*3600 - minutos*60
    return (horas, minutos, segundos)
print(f"la suma de los intervalos es: {inversor(suma)}")