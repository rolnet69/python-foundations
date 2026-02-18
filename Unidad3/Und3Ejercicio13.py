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
    
    # Crear número complejo como tupla (real, imag)
    z = (real, imag)
    opuesto = (-real, -imag)
    conjugado = (real, -imag)
    
    # Tupla: (complejo, opuesto, conjugado)
    tupla = (z, opuesto, conjugado)
    complejos.append(tupla)
    
    # Formato para mostrar
    def formato(c):
        r, i = c
        if i >= 0:
            return f"{r} + {i}j"
        else:
            return f"{r} - {abs(i)}j"
    
    print(f"Agregado: {formato(z)} | Opuesto: {formato(opuesto)} | Conjugado: {formato(conjugado)}")

# Mostrar resultados
print("\n" + "=" * 50)
print("Resultados")
print("=" * 50)

def formato(c):
    r, i = c
    if i >= 0:
        return f"{r} + {i}j"
    else:
        return f"{r} - {abs(i)}j"

for i, (z, op, conj) in enumerate(complejos, 1):
    print(f"\nTupla {i}:")
    print(f"Complejo:  {formato(z)}")
    print(f"Opuesto:   {formato(op)}")
    print(f"Conjugado: {formato(conj)}")

print("\n" + "=" * 50)
print(f"Total de números complejos Ingresados: {len(complejos)}")
print("=" * 50)