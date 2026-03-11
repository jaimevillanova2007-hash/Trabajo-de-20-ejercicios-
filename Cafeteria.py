# PROGRAMA: CAFETERIA - TOTAL DE COMPRA


# Pedir la bebida al usuario
bebida = input("Ingrese la bebida que desea (cafe, te, jugo): ")

# Pedir cuántas unidades quiere
cantidad = int(input("Ingrese la cantidad que desea comprar: "))

# Determinar el precio según la bebida
if bebida == "cafe":
    precio = 4000

elif bebida == "te":
    precio = 3500

elif bebida == "jugo":
    precio = 5000

else:
    print("Bebida no disponible")
    precio = 0

# Calcular el total
total = precio * cantidad

# Mostrar el total
print("Total a pagar:", total)