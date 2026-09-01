persona = {
    "nombre": "Amado",
    "edad": 20,
    "carrera": "Ingeniería de Sistemas y Computación",
    "ciudad": "Barranquilla"
}

print("CLAVES:")
for clave in persona.keys():
    print(clave)

print("\nVALORES:")
for valor in persona.values():
    print(valor)

print("\nCLAVE - VALOR:")
for clave, valor in persona.items():
    print(clave, ":", valor)
