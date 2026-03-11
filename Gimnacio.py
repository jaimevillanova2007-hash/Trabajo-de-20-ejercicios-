
# PROGRAMA: GIMNASIO - ACCESO POR EDAD
try:

   # Pedir edad al usuario
    edad = int(input("Ingrese su edad: "))

   # Condiciones para determinar el grupo
    if edad < 13:
     print("No puede ingresar al gimnasio")
    
    elif edad >= 13 and edad <= 17:
     print("Pertenece a la clase juvenil")

    elif edad >= 18 and edad <= 59:
     print("Pertenece a la clase general")

    else:
     print("Pertenece a la clase senior")

except ValueError:
  print("Escriba un numero valido ")