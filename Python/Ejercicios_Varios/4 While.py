venganza = input("Vicky, queres agregar mas gatos? (si/no) ")
gatos = 0
while (venganza == "si"):
    cantidad = int(input("Cuantos gatos queres agregar? "))
    gatos = gatos + cantidad
    venganza = input("Vicky, queres agregar mas gatos? (si/no) ")

print(f"vicky, has pedido {gatos} gatos")
