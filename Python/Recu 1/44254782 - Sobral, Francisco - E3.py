def ingreso_pedido_cliente(info_clientes:dict,menu_panaderia:list) -> dict:
    dni = int(input("Ingrese el numero de dni: "))
    if dni in info_clientes[dni] :
        seguir = "si"
        while seguir == "si":     
            nombre = info_clientes[dni][0]
            pedido = input("Que pidio?: ")
            deuda = menu_panaderia[pedido][0]
            cantidad = menu_panaderia[pedido][1] + 1
            seguir = input("Desea continuar ingresando pedidos? (si/no): ")
    else:
        seguir = "si"
        while seguir == "si":
            nombre = input("Nombre y Apellido: ")
            pedido = input("Que pidio?: ")
            deuda = menu_panaderia[pedido][0]
            cantidad = menu_panaderia[pedido][1] + 1
            seguir = input("Desea continuar ingresando pedidos? (si/no): ")
    print("MUchas Gracias, su pedido fue realizado.")
        
    info_clientes[dni] = [nombre,deuda]
    menu_panaderia[pedido][1] = cantidad

def ingreso_pago(info_clientes:dict) -> dict:
    dni = input("Ingrese el numero de dni: ")
    print(f"La deuda es de {info_clientes[dni][2]} pesos.")
    pago = int(input("Cuanto pago?: "))
    deuda = info_clientes[dni][2] - pago
    info_clientes[dni][2] = deuda
    
def buscar_mayores_deudas(info_clientes:dict) -> list:

    lista_deudores = dict()

    for values in info_clientes.values():
        #nombre = values[0]
        #deuda = values[1]

        if values[0] not in lista_deudores:
            lista_deudores[values[0]] = [values[1]]

    while len(lista_deudores.values()) > 4:
        lista_deudores.pop(min(lista_deudores,  key=(lista_deudores.get)))

    lista_deudores_descending_list = list(lista_deudores.items()) #Aca se arma una lista de tuplas a partir del diccionario
    lista_deudores_descending_list.sort(reverse=True, key=lambda x: x[1]) #Aca se ordena esa lista por el segundo elemento de las tuplas.
    print("")
    print(lista_deudores_descending_list)
    print("")

def reporte_cantidad_pedidos_por_articulo(menu_panaderia:dict) -> str:
    for clave, valor in menu_panaderia.items():
        print(f"{clave} - {valor[1]} pedidos.")    

def porcentaje_pedidos_mayores_de_1000(menu_panaderia:dict) -> str:
    pedido_mayor_mil = 0
    pedidos_totales = 0
    
    for articulo in menu_panaderia.values():
        if articulo[0] * articulo[1] >= 1000:
            pedido_mayor_mil += 1
            pedidos_totales += 1
        else:
            pedidos_totales += 1
    porcentaje = round(((pedido_mayor_mil/pedidos_totales)*100))
    print(f"\nEl promedio de pedidos mayores a $1000 es de {porcentaje}%.\n")

def main() -> None:
    menu_panaderia = {"Baguette_Clasica":[250,2],"Baggette_Rellena":[250,4],"Baggette_Vegana":[250,7],"Baggette_con_Muzzarella":[500,0],"Merlot":[300,2],"Vin_Rose":[300,0],"Borgoña_blanc":[550,0]}
    info_clientes = {44254782:["Francisco Sobral",0],21002041:["Juan Miguens",500],44264782:["Martin Wain",200],43254782:["Pedro Jator",1000],44259082:["Francisco Torbi",3243]}
    print( """
    a. Ingresar pedidos por cliente.
    b. Ingresar pago de pedidos de un cliente.
    c. Top 5 de las deudas más importantes. 
    d. Reporte de pedidos solicitados por articulo.
    e. Indicar el porcentaje de pedidos superiores a $1000.
    """)
    eleccion = input("Que accion desea realizar?: ")

    if eleccion == "a":
        ingreso_pedido_cliente(info_clientes,menu_panaderia)
    elif eleccion == "b":
        ingreso_pago(info_clientes)
    elif eleccion == "c":
        buscar_mayores_deudas(info_clientes)    
    elif eleccion == "d":
        reporte_cantidad_pedidos_por_articulo(menu_panaderia)
    elif eleccion == "e":
        porcentaje_pedidos_mayores_de_1000(menu_panaderia)
main()
