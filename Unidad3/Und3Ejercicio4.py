print("-----------------------------------")
print("Ejercicio 4 - Generar matriz Identidad")
print("-----------------------------------")

n = int(input("\nDimensión de la matriz (n): "))

print(f"\nCreando matriz identidad {n}x{n}:")
print("-" * 30)

matriz = []
for i in range(n):
    fila = [0] * n  
    matriz.append(fila)


print("Colocando 1's en la diagonal principal:")
for i in range(n):
    matriz[i][i] = 1  
    print(f"  Posición [{i}][{i}] = 1")


print(f"\nMatriz Identidad {n}x{n}:")
for i in range(n):
    print("  ", end="")
    for j in range(n):
        print(f"{matriz[i][j]:2}", end=" ")
    print()