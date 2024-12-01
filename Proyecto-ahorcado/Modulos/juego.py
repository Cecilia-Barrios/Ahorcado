from Modulos.monigote import mostrar_monigote

def jugar(palabras):
    import random
    idioma = input("---Seleccione el idioma (es/en)--->  ").strip().lower()
    if idioma not in ["es", "en"]:
        print("Idioma no válido. Intente nuevamente.")
        return 0

    secreta = random.choice([p[idioma] for p in palabras])
    cadena = "_" * len(secreta)
    intentos = 0
    letras_usadas = []

    while True:
        print(f"\nPalabra: {cadena}")
        print(f"Letras usadas: {', '.join(letras_usadas)}")
        print(f"Intentos restantes: {6 - intentos}")
        letra = input("Ingrese una letra: ").lower()

        if letra in letras_usadas:
            print("Ya usaste esa letra. Intenta otra.")
            continue

        letras_usadas.append(letra)

        if letra in secreta:
            for i in range(len(secreta)):
                if secreta[i] == letra:
                    cadena = cadena[:i] + letra + cadena[i+1:]
        else:
            intentos += 1
            mostrar_monigote(intentos)

        if intentos == 6:
            print("--------------------------------------------------------------------")
            print(f"\nHAS PERDIDO EL JUEGO, la palabra secreta era: **{secreta}**\n")
            print("--------------------------------------------------------------------")
            return 0
        elif cadena == secreta:
            print("--------------------------------------------------------------------")
            print(f"\n***FELICIDADES HAS GANADO EL JUEGO, la palabra secreta era: {secreta}***\n")
            print("--------------------------------------------------------------------")
            return len(secreta)