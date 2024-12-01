import json

def cargar_palabras(archivo):
    try:
        with open("Data/data.json", "r") as archivo: 
            return json.load(archivo)  
    except:
        print("ERROR, No se encontro el archivo deseado")
        return []

