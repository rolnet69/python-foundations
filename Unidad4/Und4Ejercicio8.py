import os

# Limpiar pantalla
os.system('cls' if os.name == 'nt' else 'clear')

print("-------------------------------------------------")
print("Ejercicio 8 - Map() + Vocales")
print("-------------------------------------------------")

def contar_vocales(palabra):

    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador


# PROGRAMA PRINCIPAL
palabras = []

print("\nIngresa palabras (Enter vacío para terminar):")
print("-" * 50)

while True:
    palabra = input("Ingresa palabra: ").strip()
    if palabra == "":
        break
    palabras.append(palabra)
    print(f"Palabra agregada: '{palabra}'")

if not palabras:
    print("\nNo ingresaste ninguna palabra.")
else:
    # APLICANDO MAP CON LAMBDA
    resultado = list(map(lambda p: contar_vocales(p), palabras))
    
    print("\n" + "=" * 60)
    print("Resultados")
    
    print(f"\nLista ingresada ({len(palabras)} palabras):")
    print(f"   {palabras}")
    
    print(f"\nNúmero de vocales por palabra:")
    
    for i, palabra in enumerate(palabras):
        vocales = resultado[i]
        print(f"   '{palabra}' tiene {vocales} vocal{'es' if vocales != 1 else ''}")
    
    print("=" * 60)