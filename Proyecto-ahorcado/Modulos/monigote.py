# Función para mostrar el monigote (progresivo según los intentos)
def mostrar_monigote(intentos):
    """
    Dibuja el monigote y la horca según la cantidad de intentos fallidos.

    Parámetros:
    - intentos (int): Número de intentos fallidos, entre 0 y 6.
    Representa el progreso del monigote que se dibuja en la horca.

    Comportamiento:
    - Imprime la horca junto con el monigote, añadiendo partes del cuerpo
    conforme aumentan los intentos fallidos.
    """
    print("\nMonigote:")
    # Base de la horca: estructura estática que se muestra siempre
    base_horca = [
        "  _______",
        "  |      |",
        "  |    ",  # Espacio donde irá el monigote
        "  |    ",
        "  |    ",
        "  |    ",
        "__|__  ",
    ]
    # Partes del monigote, dependiendo de los intentos fallidos
    monigote = {
        1: ["  O  "],  # Cabeza
        2: ["  O  ", "  |  "],  # Cabeza + cuerpo
        3: ["  O  ", " /|  "],  # Cabeza + cuerpo + un brazo
        4: ["  O  ", " /|\\ "],  # Cabeza + cuerpo + ambos brazos
        5: ["  O  ", " /|\\ ", " /   "],  # Cabeza + cuerpo + ambos brazos + una pierna
        6: ["  O  ", " /|\\ ", " / \\ "]  # Monigote completo
    }
        
    # Construir la horca con el monigote según los intentos
    for i in range(len(base_horca)):
        if i == 2 and intentos > 0:  # Línea donde comienza el monigote
            # Obtiene las partes del monigote correspondientes al número de intentos
            for parte in monigote.get(intentos, []):
                print(f"{base_horca[i]}{parte}")
                i += 1  # Avanzar para no sobrescribir la horca
        else:
            # Muestra las líneas restantes de la horca
            print(base_horca[i])
