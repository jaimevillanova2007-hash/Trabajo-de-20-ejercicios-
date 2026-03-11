# PROGRAMA: PARQUEADERO

horas = int(input("Ingrese cuántas horas estuvo el carro: "))

precio_primera_hora = 5000
precio_hora_extra = 3000


total = 0

for i in range(1, horas + 1):
    
    if i ==1 :
        total = total + 5000

    else :
        total = total + 3000

print("Total a pagar:", total)