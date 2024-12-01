from Modulos.monigote import mostrar_monigote
import random

def jugar(palabras):
    """
    Función principal del juego del ahorcado.

    Parámetros:
    - palabras (list): Lista de diccionarios, donde cada diccionario tiene palabras
    asociadas a diferentes idiomas. Ejemplo: [{"es": "gato", "en": "cat"}].

    Comportamiento:
    - Selecciona un idioma y una palabra secreta al azar.
    - Permite al jugador adivinar la palabra, mostrando pistas como la cantidad
    de letras y un registro de las letras usadas.
    - Finaliza cuando el jugador adivina la palabra o agota los intentos.
    
    Retorna:
    - 0: Si el jugador pierde.
    - int: La longitud de la palabra secreta si el jugador gana.
    """
    # Selección del idioma
    idioma = input("---Seleccione el idioma (es/en)--->  ").strip().lower()
    if idioma not in ["es", "en"]:
        print("Idioma no válido. Intente nuevamente.")
        return 0
        
    # Selección de la palabra secreta en el idioma elegido
    secreta = random.choice([p[idioma] for p in palabras])
    cadena = "_" * len(secreta)# Representación oculta de la palabra secreta
    intentos = 0# Contador de intentos fallidos
    letras_usadas = []# Registro de letras ya ingresadas
    
    # Ciclo principal del juego
    while True:
        print(f"\nPalabra: {cadena}")
        print(f"Letras usadas: {', '.join(letras_usadas)}")
        print(f"Intentos restantes: {6 - intentos}")
        # Solicitar una letra al jugador
        letra = input("Ingrese una letra: ").lower()
        # Verificar si la letra ya fue usada
        if letra in letras_usadas:
            print("Ya usaste esa letra. Intenta otra.")
            continue
        # Registrar la nueva letra usada
        letras_usadas.append(letra)
        # Comprobar si la letra está en la palabra secreta
        if letra in secreta:
            for i in range(len(secreta)):
                if secreta[i] == letra:
                    cadena = cadena[:i] + letra + cadena[i+1:]
        else:
            # Incrementar los intentos fallidos y mostrar el monigote
            intentos += 1
            mostrar_monigote(intentos)
        # Verificar las condiciones de fin del juego
        if intentos == 6:# Límite de intentos alcanzado
            print("--------------------------------------------------------------------")
            print(f"\nHAS PERDIDO EL JUEGO, la palabra secreta era: **{secreta}**\n")
            print("--------------------------------------------------------------------")
            return 0
        elif cadena == secreta:# Todas las letras descubiertas
            print("--------------------------------------------------------------------")
            print(f"\n***FELICIDADES HAS GANADO EL JUEGO, la palabra secreta era: {secreta}***\n")
            print("--------------------------------------------------------------------")
            return len(secreta)# Retorna la longitud de la palabra como puntuación
