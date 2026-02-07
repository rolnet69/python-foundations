print("-----------------------------------")
print("Ejercicio 2 - Producto de Matrices")
print("-----------------------------------")
fA,cA = int(input("Filas Matriz A: ")), int(input("Columnas Matriz A: "))
fB,cB = int(input("Filas Matriz B: ")), int(input("Columnas Matriz B: "))

if cA != fB: print(f"ERROR: {cA}≠{fB}"); exit()

A = [[int(input(f"A[{i+1}][{j+1}]: ")) for j in range(cA)] for i in range(fA)]
B = [[int(input(f"B[{i+1}][{j+1}]: ")) for j in range(cB)] for i in range(fB)]

R = [[sum(A[i][k]*B[k][j] for k in range(cA)) for j in range(cB)] for i in range(fA)]

print("\nMatriz A:"); [print(f) for f in A]
print("\nMatriz B:"); [print(f) for f in B]
print("\nResultado A×B:"); [print(f) for f in R]