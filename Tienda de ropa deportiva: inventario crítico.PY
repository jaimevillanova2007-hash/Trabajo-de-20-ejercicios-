# PROGRAMA: INVENTARIO
# INICIO DEL CICLO 
agotado = 0
bajo = 0
normal = 0
#INICIO DEL CICLO 
for i in range(10):

    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad disponible: "))

    if cantidad == 0:
        agotado += 1

    elif cantidad <= 5:
        bajo += 1

    else:
        normal += 1

print("Productos agotados:", agotado)
print("Stock bajo:", bajo)
print("Stock normal:", normal)