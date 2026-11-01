errores = []

print("___Validar contraseña____")

while True:
    contrasena = input("Introduce su password: ")
    errores.clear()  # Limpiamos errores del intento anterior

    # Validaciones
    if len(contrasena) < 8:
        errores.append("La contraseña debe tener al menos 8 caracteres.")
    
    if not any(char.isdigit() for char in contrasena):
        errores.append("La contraseña debe contener al menos un número.")
    
    if not any(char.isupper() for char in contrasena):
        errores.append("La contraseña debe contener al menos una letra mayúscula.")
    
    if not any(char.islower() for char in contrasena):
        errores.append("La contraseña debe contener al menos una letra minúscula.")

    # Si no hay errores, mostrar estadísticas y romper el bucle
    if not errores:
        print("¡Contraseña correcta!")

        # Contadores
        contador_mayuscula = sum(1 for letra in contrasena if letra.isupper())
        contador_minuscula = sum(1 for letra in contrasena if letra.islower())
        contador_numeros = sum(1 for letra in contrasena if letra.isdigit())
        contador_especial = sum(1 for letra in contrasena if not letra.isalnum())

        # Resultados
        print("Tiene mayúscula(s):", contador_mayuscula)
        print("Tiene minúscula(s):", contador_minuscula)
        print("Contiene número(s):", contador_numeros)
        print("Tiene carácter(es) especial(es):", contador_especial)

        break  # Rompemos el bucle

    else:
        # Mostrar errores y volver a pedir contraseña
        print("Errores encontrados:")
        for error in errores:
            print("-", error)