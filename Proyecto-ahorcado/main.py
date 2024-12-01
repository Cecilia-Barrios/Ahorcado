from Modulos.palabras import cargar_palabras
from Modulos.juego import jugar
from Modulos.puntajes import mostrar_puntajes, guardar_puntaje

# Menú principal
def mostrar_menu():
        """
    Muestra el menú principal del juego y solicita una opción al usuario.

    Retorna:
    - str: La opción seleccionada por el usuario.
    """
        print("\n--- Menú Principal ---")
        print("1. Jugar")
        print("2. Ver puntajes")
        print("3. Salir")
        return input("\n---Seleccione una opción--->  " )

if __name__ == "__main__":
    palabras = cargar_palabras("Data/data.json")

    while True:
        opcion = mostrar_menu()
        match opcion:
            case "1": # Ejecuta la opcion de jugar.
                puntaje = jugar(palabras)
                if puntaje > 0:
                    nombre = input("Ingresa tu nombre: ")
                    guardar_puntaje(nombre, puntaje, "Data/score.json")
            case "2": # Muestra los puntaje guardados
                mostrar_puntajes("Data/score.json") 
            case "3": # Termina el programa con un mensaje
                print("\n---Gracias por jugar!---")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")


