import collections


def elecciones(eleccion: str, stock_estable: dict, stock_del_dia: dict, pedidos_del_dia: dict, pedidos: dict, dia: int, caja_abierta: bool) -> None:
    if eleccion == "a":
        dia, stock_del_dia, pedidos_del_dia, caja_abierta = apertura_caja(
            caja_abierta, dia, stock_del_dia)
    elif eleccion == "b":
        nuevo_pedido(stock_del_dia, pedidos_del_dia)
    elif eleccion == "c":
        reporte_producto_mas_comprado(pedidos)
    elif eleccion == "d":
        reporte_stock_frigorifico(stock_estable)
    elif eleccion == "e":
        stock_estable, caja_abierta = cierre_caja(
            pedidos, stock_estable, stock_del_dia, pedidos_del_dia, caja_abierta)
    elif eleccion == "f":
        pronostico_quiebre_stock(dia, stock_estable, pedidos)


def apertura_caja(caja_abierta: bool, dia: int, stock_estable: dict) -> tuple:

    if caja_abierta == False:
        stock_del_dia = stock_estable.copy()
        dia += 1
        pedidos_del_dia = dict()
        caja_abierta = True
    else:
        print("Ya hay una caja abierta.")
    return dia, stock_del_dia, pedidos_del_dia, caja_abierta


def nuevo_pedido(stock_del_dia: dict, pedidos_del_dia: dict) -> None:

    seguir = "si"
    precio_total_pedido = 0
    print("Excelente, vamos a tomar su pedido.")
    while seguir == "si":
        producto = input("Producto a llevar?: ")
        frigorifico = input("Frigorifico?: ")
        cantidad_g = int(input("Ingrese la cantidad de gramos a llevar: "))
        cantidad_kg = cantidad_g/1000
        # if preductos q no se pisen
        if stock_del_dia[frigorifico][producto][0] >= cantidad_kg:
            stock_del_dia[frigorifico][producto][0] -= cantidad_kg
            precio_total_pedido += cantidad_g * \
                stock_del_dia[frigorifico][producto][1]
            if producto in pedidos_del_dia[frigorifico]:
                pedidos_del_dia[frigorifico][producto][0] += cantidad_kg
                pedidos_del_dia[frigorifico][producto][1] += precio_total_pedido
            else:
                pedidos_del_dia[frigorifico][producto] = [
                    cantidad_kg, precio_total_pedido]

        else:
            print(
                f"No fue posible procesar su pedido.\nSolo quedan {stock_del_dia[producto][frigorifico][0]} kg disponibles de ese articulo.")

        seguir = input("Desea pedir algo mas? (si/no): ")


def reporte_producto_mas_comprado(pedidos: dict) -> None:
    # producto - frigorifico - kg comprados
    # frigorifico-procucto,cantidaadkg,preciototal = pedidos

    # reporte = sorted(pedidos.items(), key=lambda x: list(x[1].values())[0], reverse=True) para ordenar dict de dict

    reporte = list()
    print("\nProducto - Frigorifico - Kg Comprados\n")
    for frigorifico in pedidos:
        for producto, info in pedidos[frigorifico].items():
            reporte.append([producto, frigorifico, info[0]])
    reporte.sort(reverse=True, key=lambda x: x[2])

    for item in reporte:
        print(f"{item[0]} - {item[1]} - {item[2]}kg")


def reporte_stock_frigorifico(stock: dict) -> None:
    reporte = list()

    frigorifico = input("Por favor ingrese un frigorifico: ")
    for frigo, valor in stock.items():
        if frigo == frigorifico:
            for producto, info in valor.items():
                reporte.append([producto, info[1]])

    reporte.sort(reverse=True, key=lambda x: x[1])

    for lista in reporte:
        print(f"{lista[0]} - ${lista[1]}")


def cierre_caja(pedidos: dict, stock_del_dia: dict, pedidos_del_dia: dict, caja_abierta: bool) -> tuple:
    ventas_totales = 0
    if caja_abierta == True:
        for clave in pedidos_del_dia.values():
            ventas_totales += clave[2]

        print(
            f"\nLas ventas del dia de hoy suman un total de ${ventas_totales}.\n")

        stock_estable = stock_del_dia.copy()
        pedidos.udate(pedidos_del_dia)
        print("\nSu caja fue cerrada con exito.\n")
    else:
        print("\nNo hay ninguna caja abierta, por favor intente nuevamente.\n")

    return stock_estable, caja_abierta


def pronostico_quiebre_stock(dia: int, stock_estable: dict, pedidos: dict) -> None:
    # frigorifico-procucto-cantidaadkg,preciototal = pedidos
    multiplicador = 30/dia
    estimado_por_producto = list()
    for frigorifico in pedidos:
        for clave, valor in pedidos[frigorifico].items():
            if clave not in estimado_por_producto:
                producto = clave
            if frigorifico not in estimado_por_producto:
                frig = frigorifico
            if valor[1] not in estimado_por_producto:
                cantidad = (valor[1]*multiplicador)
            estimado_por_producto.append([producto, frigorifico, cantidad])

    for elementos in estimado_por_producto:
        cantidad_restante = stock_estable[elementos[1]][elementos[0]][0]

        if cantidad_restante < elementos[2]:
            print(
                f"\nEl producto '{elementos[0]} - {elementos[1]}' esta en riesgo de quedarse sin stock en un mes.\n")


def main() -> None:
    pedidos = dict()
    stock_del_dia = dict()
    pedidos_del_dia = dict()
    dia = 0
    caja_abierta = False

    stock_estable = {
        "Bocatti": {"Jamon_cocido": [20, 189],
                    "Salame_milan": [3, 157]},
        "Rogiano": {"Jamon_cocido": [10, 117]},
        "Paladini": {"Jamon_crudo": [5, 113],
                     "Mortadela": [5, 90],
                     "Salame_milan": [4, 121]},
        "La_piamontesa": {"Salame_milan": [7, 118]},
        "Calchaqui": {"Mortadela": [11, 82]},
        "Trozer": {"Mortadela": [3, 49]}
    }

    eleccion = input("""
            a)Apertura de Caja.
            b)Nueva compra.
            c)Reporte Producto Más Comprado.
            d)Reporte Stock por Frigorífico.
            e)Cierre de Caja.
            f)Pronóstico de Quiebre de Stock.

            Cual de estas acciones desea realizar?: """)
    elecciones(eleccion, stock_estable, stock_del_dia,
               pedidos_del_dia, pedidos, dia, caja_abierta)

 # frigorifico-procucto,cantidaadkg,preciototal = pedidos


stock_estable = {
    "Bocatti": {"Jamon_cocido": [20, 189],
                "Salame_milan": [3, 157]},
    "Rogiano": {"Jamon_cocido": [10, 117]},
    "Paladini": {"Jamon_crudo": [5, 113],
                 "Mortadela": [5, 90],
                 "Salame_milan": [4, 121]},
    "La_piamontesa": {"Salame_milan": [7, 118]},
    "Calchaqui": {"Mortadela": [11, 82]},
    "Trozer": {"Mortadela": [3, 49]}
}

pedidos = {"Bocatti": {"Jamon_cocido": [2, 100],
                       "Salame_milan": [3, 157]},
           "Rogiano": {"Jamon_cocido": [1, 117]},
           "Paladini": {"Jamon_crudo": [5, 113],
                        "Mortadela": [5, 90],
                        "Salame_milan": [4, 121]},
           "La_piamontesa": {"Salame_milan": [7, 118]},
           "Calchaqui": {"Mortadela": [5, 82]},
           "Trozer": {"Mortadela": [3, 49]}}
reporte_producto_mas_comprado(pedidos)
