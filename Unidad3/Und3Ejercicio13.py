
import os

# Limpiar pantalla
os.system('cls' if os.name == 'nt' else 'clear')

print("----------------------------------------")
print("Ejercicio 13 - Numeros complejos")
print("----------------------------------------")

complejos = []

print("\nIngresa números complejos (parte real y parte imaginaria)")
print("Escribe 'fin' si ya no quieres ingresar números")
print("-" * 50)

while True:
    print(f"\nNúmero {len(complejos) + 1}:")
    
    # Parte real
    entrada = input("Parte real: ")
    if entrada.lower() == 'fin':
        break
    try:
        real = float(entrada)
    except ValueError:
        print("Debe ingresar un número")
        continue
    
    # Parte imaginaria
    entrada = input("Parte imaginaria: ")
    if entrada.lower() == 'fin':
        break
    try:
        imag = float(entrada)
    except ValueError:
        print("Debe ingresar un número")
        continue
    
    # Crear número complejo
    z = complex(real, imag)
    opuesto = complex(-real, -imag)
    conjugado = complex(real, -imag)
    
    # Tupla: (complejo, opuesto, conjugado)
    tupla = (z, opuesto, conjugado)
    complejos.append(tupla)
    
    print(f"Agregado: {z} | Opuesto: {opuesto} | Conjugado: {conjugado}")

# Mostrar resultados
print("\n" + "=" * 50)
print("Resultados")
print("=" * 50)

for i, (z, op, conj) in enumerate(complejos, 1):
    print(f"\nTupla {i}:")
    print(f"Complejo:  {z}")
    print(f"Opuesto:   {op}")
    print(f"Conjugado: {conj}")

print("\n" + "=" * 50)
print(f"Total de números complejos Ingresados: {len(complejos)}")
print("=" * 50)