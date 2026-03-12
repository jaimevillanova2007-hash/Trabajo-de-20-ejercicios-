# Inicializamos contadores
bajo = 0
medio = 0
alto = 0

# Registramos 5 personas
for i in range(5):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    dias = int(input("Días asistidos en la semana: "))
    minutos = int(input("Minutos promedio entrenados por día: "))
    
    # Clasificación por compromiso
    if dias < 3:
        compromiso = "bajo compromiso"
        bajo += 1
    elif 3 <= dias <= 4:
        compromiso = "compromiso medio"
        medio += 1
    else:
        compromiso = "compromiso alto"
        alto += 1
    
    print(f"{nombre} tiene {compromiso}.\n")

# Resultados finales
print("Resumen por categoría:")
print(f"Bajo compromiso: {bajo}")
print(f"Compromiso medio: {medio}")
print(f"Compromiso alto: {alto}")