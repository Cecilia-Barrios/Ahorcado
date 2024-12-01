import json

def guardar_puntaje(nombre, puntaje, archivo):
    """
    Guarda un puntaje en un archivo JSON, manteniendo solo los 5 mejores puntajes.

    Parámetros:
    - nombre (str): Nombre del jugador.
    - puntaje (int): Puntaje obtenido por el jugador.
    - archivo (str): Nombre del archivo donde se almacenan los puntajes.
    """
    try:
        # Intenta abrir el archivo y cargar los puntajes existentes
        with open(archivo, 'r') as f:
            puntajes = json.load(f)
    except:
        # Si ocurre un error (archivo no existe o está vacío), inicializa una lista vacía
        puntajes = []
    # Agrega el nuevo puntaje a la lista
    puntajes.append({"nombre": nombre, "puntaje": puntaje})
    # Ordena los puntajes de mayor a menor y conserva solo los 5 mejores
    puntajes = sorted(puntajes, key=lambda x: x["puntaje"], reverse=True)[:5]

    # Guarda la lista actualizada de puntajes en el archivo
    with open(archivo, 'w') as f:
        json.dump(puntajes, f, indent = 4)

def mostrar_puntajes(archivo):
    """
    Muestra en consola los puntajes almacenados en un archivo JSON.

    Parámetros:
    - archivo (str): Nombre del archivo donde se almacenan los puntajes.
    """
    try:
        # Intenta abrir el archivo y cargar los puntajes existentes
        with open(archivo, 'r') as f:
            puntajes = json.load(f)
        # Muestra un encabezado y los puntajes 
        print("___________________________________________")
        print("\n--- Mejores Puntajes ---\n")
        print("___________________________________________")
        for i, p in enumerate(puntajes, start=1):
            print(f"{i}. {p['nombre']} - {p['puntaje']} puntos")
    except:
        # Si ocurre un error (archivo no existe o está vacío), muestra un mensaje informativo
        print("No hay puntajes guardados aún.")
