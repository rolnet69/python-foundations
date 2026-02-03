print("-------------------------------")
print("Ejercicio 4")
print("-------------------------------")

# Inicializar variables
a = b = c = None
nombres = [("a", False), ("b", True), ("c", True)] 

for nombre, puedeSerCero in nombres:
    while True:
        entrada = input(f"Ingresa el valor de {nombre}: ").strip()
        
        entrada = entrada.replace(',', '.')
        
        if entrada.startswith('+'):
            entrada = entrada[1:]
        
        if entrada and entrada.lstrip('-').replace('.', '', 1).isdigit():
            valor = float(entrada)
            
            if not puedeSerCero and valor == 0:  
                print(f"ERROR: '{nombre}' no puede ser 0 en una ecuación cuadrática.")
            else:
                if nombre == 'a':
                    a = valor
                elif nombre == 'b':
                    b = valor
                else:
                    c = valor
                break
        
        print("ERROR: Ingresa un número válido.")

# Calcular discriminante
discriminante = b**2 - 4*a*c

print(f"\nEcuación: {a}x² + {b}x + {c} = 0")
print(f"Discriminante (Δ) = {b}² - 4*{a}*{c} = {discriminante}")

if discriminante > 0:
    # Dos soluciones reales diferentes
    x1 = (-b + discriminante**0.5) / (2*a)
    x2 = (-b - discriminante**0.5) / (2*a)
    print(f"\nDos soluciones reales diferentes:")
    print(f"x₁ = {x1}")
    print(f"x₂ = {x2}")
    
elif discriminante == 0:
    # Una solución real doble
    x = -b / (2*a)
    print(f"\nUna solución real doble:")
    print(f"x = {x}")
    
else:
    # Dos soluciones complejas
    real = -b / (2*a)
    imaginario = (-discriminante)**0.5 / (2*a)
    print(f"\nDos soluciones complejas conjugadas:")
    print(f"x₁ = {real} + {imaginario}j")
    print(f"x₂ = {real} - {imaginario}j")