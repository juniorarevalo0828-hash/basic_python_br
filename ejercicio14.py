import json


persona = {
    "nombre": "Amado",
    "edad": 20,
    "carrera": "Ingeniería de Sistemas y Computación",
    "ciudad": "Barranquilla"
}


persona_json = json.dumps(
    persona,
    indent=4,
    ensure_ascii=False
)

print(persona_json)
