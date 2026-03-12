
# PROGRAMA: HELADERIA

total_vendido = 0
clientes = 0

cono = 0
vaso = 0
banana = 0

producto = input("Producto (cono, vaso, banana, salir): ")

while producto != "salir":

    cantidad = int(input("Cantidad: "))

    if producto == "cono":
        total_vendido += 3000 * cantidad
        cono += cantidad

    elif producto == "vaso":
        total_vendido += 4000 * cantidad
        vaso += cantidad

    elif producto == "banana":
        total_vendido += 9000 * cantidad
        banana += cantidad

    else:
        print("Producto no válido")

    clientes += 1
    producto = input("Producto (cono, vaso, banana, salir): ")

print("Total vendido:", total_vendido)
print("Clientes atendidos:", clientes)

if cono > vaso and cono > banana:
    print("Producto más pedido: cono")
elif vaso > banana:
    print("Producto más pedido: vaso")
else:
    print("Producto más pedido: banana")