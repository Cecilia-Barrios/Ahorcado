import json

def cargar_palabras(archivo):
    """
    Carga una lista de palabras desde un archivo JSON.

    Parámetros:
    - archivo (str): Ruta del archivo JSON que contiene las palabras.

    Retorna:
    - list: Lista de palabras cargadas desde el archivo JSON.
    Si ocurre un error (por ejemplo, si el archivo no existe), retorna una lista vacía.
    """
    try:
        # Intenta abrir el archivo JSON en modo lectura
        with open("Data/data.json", "r") as archivo: 
            # Carga y devuelve el contenido del archivo como un objeto Python
            return json.load(archivo)  
    except:
        # Si ocurre un error, muestra un mensaje de error
        print("ERROR, No se encontro el archivo deseado")
        # Retorna una lista vacía como valor por defecto
        return []

