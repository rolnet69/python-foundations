import os

# Limpiar pantalla
os.system('cls' if os.name == 'nt' else 'clear')

print("=" * 60)
print("Ejercicio 9 - PANCAKE SORTING")
print("=" * 60)


def pancake_sort(pila):

    pila = pila[:]
    secuencia = []
    n = len(pila)

    print(f"\nPila inicial: {pila}")
    print("-" * 50)

    for tamaño in range(n, 1, -1):
        # Encontrar el panqueque más grande en la subpila actual
        idx_max = pila[:tamaño].index(max(pila[:tamaño]))

        if idx_max == tamaño - 1:
            print(f"El {pila[idx_max]} ya está abajo")
            continue

        # Si no está arriba, voltear para llevarlo arriba
        if idx_max != 0:
            print(f"\nVoltear posición {idx_max + 1}: ", end="")
            pila[:idx_max + 1] = pila[:idx_max + 1][::-1]
            secuencia.append(idx_max + 1)
            print(pila)

        # Voltear para llevarlo abajo
        print(f"Voltear posición {tamaño}: ", end="")
        pila[:tamaño] = pila[:tamaño][::-1]
        secuencia.append(tamaño)
        print(pila)

    print("\n" + "=" * 50)
    print(f"Pila ordenada: {pila}")
    print(f"Secuencia de volteos: {secuencia}")
    return secuencia, pila


# PROGRAMA PRINCIPAL
entrada = input("\nIngresa los diámetros (separados por espacio): ")
pancakes = [int(x) for x in entrada.split()]

if pancakes:
    pancake_sort(pancakes)
else:
    print("No ingresaste ningún panqueque.")

print("\n" + "=" * 60)