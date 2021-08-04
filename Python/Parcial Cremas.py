def introduccir_cantidad_crema_disponible(cisternas:dict) -> dict:
    for articulo in cisternas:
        nueva_cantidad = int(input(f"Por favor ingrese la cantidad disponible del articulo {articulo}: "))
        cisternas[articulo][1] = nueva_cantidad

def ingresar_crema_a_utilizar(cisternas:dict,cremas:dict) -> dict:
    pedido_posible = True
    while pedido_posible:
        crema = int(input(f"Que crema desea solicitar (por codigo): "))
        envase = int(input("Que tipo de envase va a llevar? (200cm3,500cm3,100cm3): "))
        cantidad_envases = int(input("Cuantos envases desea llevar?: "))
        cantidad_pedida = envase * cantidad_envases
        if cantidad_pedida < cisternas[crema]:
            cisternas[crema][1] -= cantidad_pedida
            mas_pedido = min(cisternas,  key=(cisternas.get))
            print(f"\nLa crema mas producida fue el {mas_pedido} - {cisternas[mas_pedido][0]}.\n")
            envase_mas_producido(cremas)
            sobrante_cada_tanque(cisternas)
            pedido_posible = False

def envase_mas_producido(cremas:dict) -> str:
    valor_total = 0
    maximo = 0
    for clave, envase in cremas.items():
        for valor in envase.values():
            valor_total += valor[1]
        if valor_total > maximo:
            maximo = valor_total
            clave_final = clave
        valor_total = 0 
    print(f"{clave_final} - {maximo} producidos.")   
        
def sobrante_cada_tanque(cisternas:dict) -> str:
    for clave, valor in cisternas.items():
        min(valor[0])
        print(f"{clave} - {valor[0]}cm3 restantes.") 

def main():
    cisternas = {100:["Humectante_clasica",0],200:["Antiage_colageno",0],300:["Facial_con_UV",0],400:["Desmaquillante",0],10:["Vitamina_A",0]}
    cremas = {
        200:{100:["Humectante_clasica",5],200:["Antiage_colageno",0],300:["Facial_con_UV",2],400:["Desmaquillante",0],10:["Vitamina_A",0]},
        500:{100:["Humectante_clasica",0],200:["Antiage_colageno",1],300:["Facial_con_UV",0],400:["Desmaquillante",0],10:["Vitamina_A",0]},
        1000:{100:["Humectante_clasica",0],200:["Antiage_colageno",0],300:["Facial_con_UV",4],400:["Desmaquillante",0],10:["Vitamina_A",0]}
        }
    introduccir_cantidad_crema_disponible(cisternas) 
    ingresar_crema_a_utilizar(cisternas,cremas)

main()