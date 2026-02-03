print("-------------------------------")
print("Ejercicio 7")
print("-------------------------------")

texto = input("Ingresa una cadena de caracteres: ")

letra_valida = False
while not letra_valida:
    letra = input("Ingresa la letra a buscar: ")
    
    # Verificar que se ingresó solo una letra
    if len(letra) != 1 or not letra.isalpha():
        print("ERROR: Debes ingresar solo una letra (a-z, A-Z).")
        print("       Intenta nuevamente.\n")
    else:
        letra_valida = True

# Contar cuántas veces aparece la letra
contador = 0
textoSinLetra = ""

for caracter in texto:
    if caracter == letra:
        contador += 1
    else:
        textoSinLetra += caracter

if contador == 1:
    veces = "vez"
else:
    veces = "veces"

print(f"\nResultados:")
print(f"La letra '{letra}' aparece {contador} {veces} en el texto.")
print(f"Texto sin la letra '{letra}': {textoSinLetra}")