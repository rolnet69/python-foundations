import os

# Limpiar pantalla
os.system('cls' if os.name == 'nt' else 'clear')

print("-----------------------------------")
print("Ejercicio 10 - Trabajando con listas")
print("-----------------------------------")

def crear_lista(n):
    lst = []
    print(f"\nLista {n}:")
    while True:
        e = input("Elemento (fin - para salir): ")
        if e == "fin": break
        try: e = int(e)
        except: pass
        lst.append(e)
        print(f"→ {lst}")
    return lst

l1 = crear_lista(1)
l2 = crear_lista(2)
resultado =[]

ambas = [x for x in l1 if x in l2]
una = [x for x in l1 if x not in l2] + [x for x in l2 if x not in l1]
r1 = [x for x in l1 if x not in l2]
r2 = [x for x in l2 if x not in l1]

resultado.append(len(ambas))
resultado.append(len(una))
resultado.append(len(r1))
resultado.append(len(r2))

print("\n" + "=" * 60)
print("Entradas:")
print(f"Lista 1: {l1}")
print(f"Lista 2: {l2}\n")
print(f"Resultado:\n {resultado}\n")
print(f"1. {len(ambas)} elementos en ambas matrices: {ambas}")
print(f"2. {len(una)} elementos en una sola matriz: {una}")
print(f"3. {len(r1)} elementos restantes en la matriz 1: {r1}")
print(f"4. {len(r2)} elementos restantes en la matriz 2: {r2}")
print("=" * 60)