print("-----------------------------------")
print("Ejercicio 3 - Suma de columnas")
print("-----------------------------------")


n = int(input("Filas: "))
m = int(input("Columnas: "))

print(f"\nIngrese matriz {n}x{m}:")
matriz = [[int(input(f"[{i+1}][{j+1}]: ")) for j in range(m)] for i in range(n)]

print("\nMatriz:")
[print(fila) for fila in matriz]

print("\nSumas:")
for j in range(m):
    suma = sum(matriz[i][j] for i in range(n))
    print(f"Columna {j+1}: {suma}", end="")
    if suma > 50:
        print(f" ← La columna {j+1} ha excedido la cantidad")
    else:
        print()