print("-----------------------------------")
print("Ejercicio 4 - Generar matriz Identidad")
print("-----------------------------------")

n = int(input("\nDimensión de la matriz (n): "))

print(f"\nCreando matriz identidad {n}x{n}:")
print("-" * 30)

# Crear matriz de ceros primero
matriz = []
for i in range(n):
    fila = [0] * n  # Fila de n ceros
    matriz.append(fila)

# Colocar 1's en la diagonal principal
print("Colocando 1's en la diagonal principal:")
for i in range(n):
    matriz[i][i] = 1  # Diagonal: fila i, columna i
    print(f"  Posición [{i}][{i}] = 1")

# Mostrar resultado
print(f"\nMatriz Identidad {n}x{n}:")
for i in range(n):
    print("  ", end="")
    for j in range(n):
        print(f"{matriz[i][j]:2}", end=" ")
    print()