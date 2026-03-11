# PROGRAMA: CINE - PRECIO DE ENTRADA

# Pedir la edad del cliente
edad = int(input("Ingrese su edad: "))

# Determinar el precio según la edad
if edad < 12:
    precio = 8000
    print("Entrada para niño")

elif edad >= 12 and edad <= 59:
    precio = 12000
    print("Entrada para adulto")

else: edad >= 60 and edad <= 100:
    precio = 9000
    print("Entrada para adulto mayor")

# Mostrar el precio
print("El precio de la entrada es:", precio)