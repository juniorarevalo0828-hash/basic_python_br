try:
    with open("datos.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

        print("Contenido del archivo:")
        print(contenido)

except FileNotFoundError:
    print("Error: El archivo datos.txt no fue encontrado.")

except Exception as error:
    print("Ocurrió un error:", error)
