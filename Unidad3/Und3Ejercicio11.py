import os

# Limpiar pantalla
os.system('cls' if os.name == 'nt' else 'clear')

print("-----------------------------------")
print("Ejercicio 11 - Guardar palabras en tupla")
print("-----------------------------------")

p = []
while True:
    e = input("Ingresa una palabra - (vacía para salir): ").strip()
    if e == "": break
    if " " in e:
        print("Solo debes ingresar una palabra")
        continue
    p.append(e)

t = tuple(p)
if t:
    a, *_, b = t
    print("\n" + "=" * 40)
    print(f"Tupla: {t}")
    print(f"Primera: {a}")
    print(f"Última: {b}")
else:
    print("\nNo hay palabras ingresadas en la tupla")