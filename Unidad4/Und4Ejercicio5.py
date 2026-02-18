import os

# Limpiar pantalla
os.system('cls' if os.name == 'nt' else 'clear')

print("-------------------------------------------------")
print("Ejercicio 5 - Torres de Hanoi.")
print("-------------------------------------------------")

def hanoi_calcular_movimientos(n, origen, destino, auxiliar):

    if n == 0:
        return 0
    if n == 1:
        return 1
    return (hanoi_calcular_movimientos(n - 1, origen, auxiliar, destino) + 
            1 + 
            hanoi_calcular_movimientos(n - 1, auxiliar, destino, origen))


def hanoi_mostrar_movimientos(n, origen, destino, auxiliar):

    if n == 1:
        print(f"Mover el disco 1 de la varilla {origen} a la varilla {destino}")
    else:
        hanoi_mostrar_movimientos(n - 1, origen, auxiliar, destino)
        print(f"Mover el disco {n} de la varilla {origen} a la varilla {destino}")
        hanoi_mostrar_movimientos(n - 1, auxiliar, destino, origen)


# PROGRAMA PRINCIPAL

# Validación de entrada (0-20)
while True:
    try:
        n = int(input("n = "))
        if 0 <= n <= 20:
            break
        else:
            print("El número debe estar entre 0 y 20")
    except ValueError:
        print("Ingresa un número entero válido")

print()
if n == 0:
    print("No se hará ningún paso")
    total = 0
else:
    
    total_calculado = hanoi_calcular_movimientos(n, 1, 3, 2)
    
    total = total_calculado
    
    if n == 1:
        print(f"Para n = 1, se realizará 1 paso en total.")
        print("El paso es el siguiente:")
        hanoi_mostrar_movimientos(n, 1, 3, 2)
    elif n <= 5:
        print(f"Para n = {n}, se realizarán {total} pasos en total.")
        print("Los pasos son los siguientes:")
        hanoi_mostrar_movimientos(n, 1, 3, 2)
    else:
        print(f"Para n = {n}, se realizarán {total} pasos en total.")
        print(f"(No se muestran los {total} movimientos por ser demasiados)")
    
    print(f"\n")
    print(f"Resultado:")
    print(f"Total de pasos: {total_calculado}")


print("\n" + "=" * 50)