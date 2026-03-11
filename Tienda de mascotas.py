# PROGRAMA: TIENDA DE MASCOTAS

# Pedir el tipo de mascota
mascota = input("Ingrese el tipo de mascota (perro, gato, conejo): ")

# Mostrar recomendación de alimento
if mascota == "perro":
    print("Recomendación: alimento para perro con proteína.")

elif mascota == "gato":
    print("Recomendación: alimento para gato rico en pescado.")

elif mascota == "conejo":
    print("Recomendación: heno y vegetales frescos.")

else:
    print("Mascota no reconocida.")