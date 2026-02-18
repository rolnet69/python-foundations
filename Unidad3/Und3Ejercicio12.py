import os

# Limpiar pantalla
os.system('cls' if os.name == 'nt' else 'clear')

print("----------------------------------------")
print("Ejercicio 12 - Puntos en el espacio (3D)")
print("----------------------------------------")

# Validar número de puntos
while True:
    try:
        n = int(input("\n¿Cuántos puntos en el espacio (3D) deseas ingresar? "))
        if n > 0:
            break
        else:
            print("Debe ingresar un número entero positivo.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")

puntos = []

for i in range(n):
    print(f"\nIngresa las coordenadas del punto {i+1}")
    
    # Validar x
    while True:
        try:
            x = float(input("  x: "))
            break
        except ValueError:
            print("Debe ingresar un número válido.")
    
    # Validar y
    while True:
        try:
            y = float(input("  y: "))
            break
        except ValueError:
            print("Debe ingresar un número válido.")
    
    # Validar z
    while True:
        try:
            z = float(input("  z: "))
            break
        except ValueError:
            print("Debe ingresar un número válido.")
    
    # Determinar signos
    sx = 'pos' if x > 0 else 'neg' if x < 0 else 'cero'
    sy = 'pos' if y > 0 else 'neg' if y < 0 else 'cero'
    sz = 'pos' if z > 0 else 'neg' if z < 0 else 'cero'
    
    # Diccionario de octantes
    octantes = {
        ('pos', 'pos', 'pos'): 'I',
        ('neg', 'pos', 'pos'): 'II',
        ('neg', 'neg', 'pos'): 'III',
        ('pos', 'neg', 'pos'): 'IV',
        ('pos', 'pos', 'neg'): 'V',
        ('neg', 'pos', 'neg'): 'VI',
        ('neg', 'neg', 'neg'): 'VII',
        ('pos', 'neg', 'neg'): 'VIII'
    }
    
    # Buscar octante
    o = octantes.get((sx, sy, sz), 'eje/plano')
    
    puntos.append((x, y, z, o))

print("\n" + "=" * 50)
print("Resultado")
print("=" * 50)

for x, y, z, o in puntos:
    if o == 'eje/plano':
        print(f"El punto ({x}, {y}, {z}) está sobre un eje o plano")
    else:
        print(f"El punto ({x}, {y}, {z}) pertenece al octante {o}")

print("\n" + "=" * 50)
print(f"Total de puntos: {len(puntos)}")
print("=" * 50)