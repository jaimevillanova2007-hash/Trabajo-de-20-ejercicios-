
# pARQUEADERO : CONTROSL DE LOS VEHICULOS 

# contador del coienzo 

total_recaudado = 0
cont_carros = 0
cont_motos = 0
max_pago = 0
vehiculo_max = ""

# inicio del ciclo 

for i in range(8):
    placa = input(f"Ingrese la placa del vehículo {i+1}: ")
    tipo = input("Tipo (carro/moto): ").lower()
    horas = int(input("Horas parqueado: "))
    
# tipos de vehiculos 

    if tipo == "carro":
        pago = horas * 4000
        cont_carros += 1
    elif tipo == "moto":
        pago = horas * 2000
        cont_motos += 1
    else:
        print("Tipo no válido, se omite el vehículo.")
        continue

    total_recaudado += pago

    if pago > max_pago:
        max_pago = pago
        vehiculo_max = placa

print(f"Total recaudado: {total_recaudado}")
print(f"Carros: {cont_carros}, Motos: {cont_motos}")
print(f"Vehículo que pagó más: {vehiculo_max} con {max_pago}")