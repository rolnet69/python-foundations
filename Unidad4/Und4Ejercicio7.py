import os

# Limpiar pantalla
os.system('cls' if os.name == 'nt' else 'clear')

print("----------------------------------------------------")
print("Ejercicio 7 - Filter + Lambda (Divisores optimizado)")
print("----------------------------------------------------")

# FUNCIÓN OPTIMIZADA PARA CONTAR DIVISORES - O(√n)
def contar_divisores(n):

    if n == 0:
        return 0
    
    n = abs(n)
    contador = 0
    
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i == n // i:  # Caso cuadrado perfecto
                contador += 1
            else:            # i y su par n//i
                contador += 2
    
    return contador


# PROGRAMA PRINCIPAL
numeros = []

print("\nIngresa números enteros (ingresa 0 para terminar):")
print("-" * 50)

while True:
    try:
        num = int(input("Ingresa un número: "))
        if num == 0:
            break
        numeros.append(num)
        print(f"Número agregado: {num} (tiene {contar_divisores(num)} divisores)")
    except ValueError:
        print("Debes ingresar un número entero")

if not numeros:
    print("\nNo ingresaste ningún número.")
else:
    # APLICANDO FILTER CON LAMBDA
    resultado = list(filter(lambda x: contar_divisores(x) > 5, numeros))
    
    print("\n" + "=" * 60)
    print("Resultados")
    print("=" * 60)
    
    print(f"\nLista ingresada ({len(numeros)} números):")
    print(f"   {numeros}")
    
    print(f"\nNúmeros filtrados con más de 5 divisores ({len(resultado)} números):")
    print(f"   {resultado}")
    print("=" * 60)
   
