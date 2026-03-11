# PROGRAMA: HELADERIA

total_vendido = 0
clientes = 0

cono = 0
vaso = 0
banana = 0

while True:

    producto = input("Ingrese producto (cono, vaso, banana) o 'salir': ")

    if producto == "salir":
        break

    cantidad = int(input("Ingrese cantidad: "))

    if producto == "cono":
        precio = 3000
        cono = cono + cantidad

    elif producto == "vaso":
        precio = 4000
        vaso = vaso + cantidad

    elif producto == "banana":
        precio = 9000
        banana = banana + cantidad

    else:
        print("Producto no válido")
        continue

    total = precio * cantidad
    total_vendido = total_vendido + total
    clientes = clientes + 1

print("Total vendido:", total_vendido)
print("Clientes atendidos:", clientes)

if cono > vaso and cono > banana:
    print("Producto más pedido: cono")
elif vaso > banana:
    print("Producto más pedido: vaso")
else:
    print("Producto más pedido: banana split")