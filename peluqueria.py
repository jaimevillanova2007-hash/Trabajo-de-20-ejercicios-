# PROGRAMA: TURNO DEL DIA

hora = int(input("Ingrese la hora de llegada (0-23): "))

if hora >= 6 and hora <= 11:
    print("Turno de la mañana")

elif hora >= 12 and hora <= 17:
    print("Turno de la tarde")

elif hora >= 18 and hora <= 22:
    print("Turno de la noche")

else:
    print("Fuera de horario")