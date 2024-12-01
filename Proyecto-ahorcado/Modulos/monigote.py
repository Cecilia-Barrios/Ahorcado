# Función para mostrar el monigote (progresivo según los intentos)
def mostrar_monigote(intentos):
    print("\nMonigote:")
    base_horca = [
        "  _______",
        "  |      |",
        "  |    ",  # Espacio donde irá el monigote
        "  |    ",
        "  |    ",
        "  |    ",
        "__|__  ",
    ]
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
            for parte in monigote.get(intentos, []):
                print(f"{base_horca[i]}{parte}")
                i += 1  # Avanzar para no sobrescribir la horca
        else:
            print(base_horca[i])