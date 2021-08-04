def carga_modificacion_pedido(stock:dict,pedidos:dict) -> None:
    eleccion = input("Que desea hacer: Cargar un pedido o modificar uno exsistente? (a/b): ")
    if eleccion == "a":
        carga_pedido(stock,pedidos)
    elif eleccion == "b":
        modificacion_pedido(stock,pedidos)
    else:
        print("Esa opcion no es correcta.")

def carga_pedido(stock:dict,pedidos:dict) -> None:
    seguir = "si"
    print("Excelente, vamos a tomar su pedido.")
    nro_cuenta = int(input("Nro cuenta?: "))
    razon_social = input("Razon social?: ")
    valor_total = 0

    while seguir == "si":
        articulo = int(input("articulo?: "))
        color = input("color?: ")
        cantidad = int(input("kg pedidos??: "))
        pedidos[nro_cuenta] = [razon_social,[(articulo[color],cantidad)]]
        precio = stock[articulo][color][2]
        valor_total += precio * cantidad
        seguir = input("Desea agregar otro pedido? (si/no): ")
    pedidos[nro_cuenta][2] = valor_total

def modificacion_pedido(stock:dict,pedidos:dict) -> None:
    seguir = "si"
    while seguir == "si":
        print(pedidos)
        nro_cuenta = int(input("\ningrese el numero de cuenta del pedido a modificar: "))
        print(pedidos[nro_cuenta][1])
        pedido_a_modificar = int(input("\n cual desea modificar?:"))


        nuevo_articulo = int(input("articulo nuevo?: "))
        color = input("color?: ")
        cantidad = int(input("kg pedidos??: "))
        pedidos[nro_cuenta][1][pedido_a_modificar] = [nuevo_articulo[color],cantidad]
        precio = stock[nuevo_articulo][color][2]
        valor_total = precio * cantidad
        pedidos[nro_cuenta][2] = valor_total
        seguir = input("Desea modificar algo mas?: ")
       
def carga_modificacion_stock(stock:dict) -> None:
    eleccion = input("Que desea hacer: Cargar stock o modificar el stock exsistente? (a/b): ")
    if eleccion == "a":
        carga_stock(stock)
    elif eleccion == "b":
        modificacion_stock(stock)
    else:
        print("Esa opcion no es correcta.")

def carga_stock(stock:dict) -> None:
    seguir = "si"
    print("Excelente, vamos a cargar stock nuevo.")

    while seguir == "si":
        cod_producto = int(input("Codigo producto?: "))
        descrpcion = input("descrpcion?: ")
        color = input("color?: ")
        kilos_dispoibles = int(input("kg disponibles??: "))
        precio = int(input("Precio x kg?: "))
        stock[cod_producto][color] = [descrpcion,kilos_dispoibles,precio]

        seguir = input("Desea agregar otro pedido? (si/no): ")

def modificacion_stock(stock) -> None:
    seguir = "si"
    modificacion_mismo_producto = "si"
    while seguir == "si":
        print(stock)
        cod_producto = int(input("\ningrese el codigo del producto a modificar: "))
        print(stock[cod_producto])
        color_a_modificar = int(input("\n Ingrese el color a modificar?: "))

        while modificacion_mismo_producto == "si:":
            print(stock[cod_producto][color_a_modificar])
            eleccion = print("""
            a) Modificar descripcion.
            b) Modificar kilos disponibles.
            c) Modificar precio por kilo.
            """)
            if eleccion == "a":
                descr_nueva = input("ingrese la nueva descripcion: ")
            elif eleccion == "b":
                kilos_disponilbes = int(input("Ingrese los kilos disponibles: "))
            elif eleccion == "c":
                precio = int(input("Ingrese el nuevoprecio por kilo."))
            stock[cod_producto][color_a_modificar] = [descr_nueva,kilos_disponilbes,precio]
            modificacion_mismo_producto = input("Desea modificar algo mas de este produto?: ")

        seguir = input("Desea modificar algo mas?: ")

def mayor_valorizacion(pedidos:dict) -> None:
    precio_pedido = {}
    for values in pedidos.values():
        #precio total = values[2]
        if values[2] not in precio_pedido:
            precio_pedido[values[2]] = [values[1]]
    
    mayor_pedido = max(precio_pedido)
    print(f"El mayor pedido fue de {mayor_pedido}")

def imprimir_pedidos(pedidos:dict) -> None:
    pedidos_organizados = {}
    for items in pedidos.values():
        if items[2] not in pedidos_organizados:
            pedidos_organizados[items[2]] = items[1]
    for clave, valor in pedidos_organizados.items():
        print(f"{valor} - ${clave} totales.") 

def main():
    #sotck = cod producto:color:(descripicion, kilos disponiobles, precio x kilo.)
    stock = {
        271:{"Crudo":["reb100% algodon peinado", 1500, 825],
        "Negro":["reb100% algodon peinado", 150, 980],
        "Azul marino":["reb100% algodon peinado", 500, 980],
        "Blanco":["reb100% algodon peinado", 100, 825]},
        433:{"Rosa":["jersey 100% algodon peinado", 300, 788],
            "Blanco":["jersey 100% algodon peinado", 30, 788]}
    }
    #nro cuenta:[razon social,pedido,valor total]
    pedidos = {4456877:["Animasana",[(stock[271]["Crudo"],1),(stock[433]["Blanco"],1)],322123],
               23567897:["sancor",[(stock[433]["Rosa"],1),(stock[433]["Blanco"],1)],1032]
               }

    eleccion = input("""
            a)Carga o modificacion de un pedido.
            b)Carga o modificacion de stock exsistente.
            c)Listar los pedidos de un nro de cuenta o razon social dada.
            d)Mostar el pedido cuya valorizacion sea la mayor.
            e)Listar todos los pedidos cargados.

            Cual de estas acciones desea realizar?: """)
    if eleccion == "a":
        carga_modificacion_pedido(stock,pedidos)
    elif eleccion == "b":
        carga_modificacion_stock(stock,pedidos)
    elif eleccion == "c":
        num_cuenta = input("Ingrese un nmro de cuenta: ")
        print(pedidos[num_cuenta[1]])
    elif eleccion == "d":
        mayor_valorizacion(pedidos)
    elif eleccion == "e":
        imprimir_pedidos(pedidos)
main()