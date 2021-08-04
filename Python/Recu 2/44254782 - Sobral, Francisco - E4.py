def analizar_precio_total(precios:dict,productos_tirados:str) -> str:
    lista_prod_tirados = productos_tirados.split(" ")
    valor_total = 0

    for producto in lista_prod_tirados:
        for key in precios.keys():
            if producto[1] == key[0]:
                cantidad = int(producto[0])
                precio = (precios[key])
                valor_total += precio * cantidad


    print(f"El valor a pagar es de ${valor_total}.")


def main() -> None:
    precios = {"Tomate":35,"Banana":20,"Kiwi":70,"Manzana":30,"Pera":25}
    productos_tirados = input("Ingrese los productos tirados: ") 
    analizar_precio_total(precios,productos_tirados)

main()

    


