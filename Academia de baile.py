# PROGRAMA: ASISTENCIA ACADEMIA

clases = int(input("Ingrese cuántas clases asistió en el mes: "))

if clases < 5:
    print("Asistencia baja")

elif clases >= 5 and clases <= 8:
    print("Asistencia media")

else:
    print("Asistencia alta")