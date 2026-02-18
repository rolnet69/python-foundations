print("-----------------------------------")
print("Ejercicio 8 - Dragon Ball API")
print("-----------------------------------")

import urllib.request
import json

#Consumo la API aon URLLIB me dio error con pip install requests
endpoint = "https://dragonball-api.com/api/characters?limit=58"
response = urllib.request.urlopen(endpoint)
data = json.loads(response.read())

#Agrupar por raza
razas = {}

for personaje in data["items"]:
    raza = personaje["race"]
    nombre = personaje["name"]
    
    # Limpiar ki (eliminar puntos y comas)
    ki_str = personaje["ki"]
    ki_limpio = ""
    for c in ki_str:
        if c.isdigit():
            ki_limpio += c
    
    ki = int(ki_limpio) if ki_limpio else 0
    
    if raza not in razas:
        razas[raza] = {"personajes": [], "suma_ki": 0, "total": 0}
    
    razas[raza]["personajes"].append({"nombre": nombre, "ki": ki})
    razas[raza]["suma_ki"] += ki
    razas[raza]["total"] += 1

#Imorimir los resultados
print("=" * 60)
print("Personajes por raza")
print("=" * 60)

for raza, info in razas.items():
    print(f"\n{raza.upper()}")
    print("-" * 60)
    
    for p in info["personajes"]:
        print(f"{p['nombre']:25} Ki: {p['ki']:>15,}")
    
    promedio = info["suma_ki"] // info["total"]
    print(f"\nPromedio de Ki: {promedio:>15,}")
    print("-" * 60)

print("\n" + "=" * 60)
print(f"Total: {len(razas)} razas | {data['meta']['totalItems']} personajes")
print("=" * 60)