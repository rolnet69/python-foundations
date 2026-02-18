import os

# Limpiar pantalla
os.system('cls' if os.name == 'nt' else 'clear')

print("-------------------------------------------------")
print("Ejercicio 3 - Contar frecuencia de cada carácter.")
print("-------------------------------------------------")

def contar_caracteres(texto):

    d = {}
    for c in texto:
        d[c] = d.get(c, 0) + 1
    return d

# Programa principal
texto = input("Ingresa un texto: ")
if texto:
    for c, n in contar_caracteres(texto).items():
        print(f"'{c}': {n}")