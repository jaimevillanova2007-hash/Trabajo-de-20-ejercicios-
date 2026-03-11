# -----------------------------------------
# PROGRAMA: INVENTARIO SIMPLE
# -----------------------------------------

# Solicitar el nombre del producto
# El nombre se guarda en una variable tipo string
nombre = input("Ingrese el nombre del producto: ")

# -----------------------------------------
# Solicitar el precio del producto
# Se valida que el usuario ingrese un número
# -----------------------------------------
while True:
    precio = input("Ingrese el precio del producto: ")
    
    try:
        precio = float(precio)  # Convertir a número decimal
        break  # Si es válido, salir del ciclo
    except:
        print("Error: Ingrese un número válido para el precio.")

# -----------------------------------------
# Solicitar la cantidad del producto
# Se valida que el usuario ingrese un número entero
# -----------------------------------------
while True:
    cantidad = input("Ingrese la cantidad del producto: ")
    
    try:
        cantidad = int(cantidad)  # Convertir a número entero
        break  # Si es válido, salir del ciclo
    except:
        print("Error: Ingrese un número entero válido para la cantidad.")

# -----------------------------------------
# Calcular el costo total del producto
# -----------------------------------------
costo_total = precio * cantidad

# -----------------------------------------
# Mostrar los resultados en consola
# -----------------------------------------
print("\n----- RESULTADO DEL INVENTARIO -----")
print("Producto:", nombre)
print("Precio unitario:", precio)
print("Cantidad:", cantidad)
print("Costo total:", costo_total)

# Mostrar también el formato solicitado en una sola línea
print("\nProducto:", nombre, "| Precio:", precio, "| Cantidad:", cantidad, "| Total:", costo_total)

# -----------------------------------------
# DESCRIPCIÓN DEL PROGRAMA
# Este programa solicita al usuario el nombre de un producto,
# su precio y la cantidad disponible en inventario.
# Luego calcula el costo total multiplicando el precio por la cantidad
# y muestra todos los datos en la consola.
# También valida que el precio y la cantidad sean números válidos.
# -----------------------------------------