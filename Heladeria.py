# PROGRAMA: HELADERIA - SABOR MAS PEDIDO

# Contadores de cada sabor
vainilla = 0
chocolate = 0
fresa = 0

# Ciclo para registrar 5 clientes
for i in range(0,5,1):
    sabor = input("Ingrese el sabor (vainilla, chocolate, fresa): ")

    # Condicionales para contar cada sabor
    if sabor == "vainilla":
        vainilla = vainilla + 1
    elif sabor == "chocolate":
        chocolate = chocolate + 1
    elif sabor == "fresa":
        fresa = fresa + 1
    else:
        print("Sabor no válido")

# Mostrar resultados
print("\nRESULTADOS DE PEDIDOS")
print("Vainilla:", vainilla)
print("Chocolate:", chocolate)
print("Fresa:", fresa)