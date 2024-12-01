import json

def guardar_puntaje(nombre, puntaje, archivo):
    try:
        with open(archivo, 'r') as f:
            puntajes = json.load(f)
    except:
        puntajes = []

    puntajes.append({"nombre": nombre, "puntaje": puntaje})
    puntajes = sorted(puntajes, key=lambda x: x["puntaje"], reverse=True)[:5]

    with open(archivo, 'w') as f:
        json.dump(puntajes, f)

def mostrar_puntajes(archivo):
    try:
        with open(archivo, 'r') as f:
            puntajes = json.load(f)
        print("--- Mejores Puntajes ---\n")
        for i, p in enumerate(puntajes, start=1):
            print(f"{i}. {p['nombre']} - {p['puntaje']} puntos")
    except:
        print("No hay puntajes guardados aún.")