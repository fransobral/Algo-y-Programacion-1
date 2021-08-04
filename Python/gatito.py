gatitos = 0
palabra = input("Introduzca una palabra:")
letras = list(palabra)
for i in range(len(letras)):
    if ((i+5) < len(letras)):
        palabra = "".join([letras[i],letras[i+1],letras[i+3],letras[i+5]])
        if (palabra == "gaio"):
            gatitos += 1
    else:
        print("No se encontraron matches.")
print(gatitos)