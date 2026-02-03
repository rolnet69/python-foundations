print("-------------------------------")
print("Ejercicio 2")
print("-------------------------------")

lados = []
nombres = ["primer lado (x)", "segundo lado (y)", "tercer lado (z)"] 

for nombre in nombres:
    while True:
        entrada = input(f"Ingresa la longitud del {nombre}: ").strip()
        
        entrada = entrada.replace(',', '.')
        
        if entrada.startswith('+'):
            entrada = entrada[1:]
        
        if entrada and entrada.lstrip('-').replace('.', '', 1).isdigit():
            valor = float(entrada)
            if valor > 0:
                lados.append(valor)
                break
        
        print("ERROR: Ingresa un número positivo")

# Asignar a variables individuales
x, y, z = lados

# Verificar desigualdad triangular
if (x + y > z) and (x + z > y) and (y + z > x):
    # Clasificar el triángulo
    if x == y == z:
        print("Clasificacion: Triángulo equilátero (todos los lados iguales)")
    elif x == y or x == z or y == z:
        print("Clasificacion: Triángulo isósceles (dos lados iguales)")
    else:
        print("Clasificacion: Triángulo escaleno (todos los lados distintos)")
else:
    print("ERROR: Estas longitudes no pueden formar un triángulo.")
    print()
    print("Se evaluaron las desigualdades triangulares:")
    print(f"  x + y = {x} + {y} = {x + y} > z ({z}) ? → {'SÍ' if x + y > z else 'NO'}")
    print(f"  x + z = {x} + {z} = {x + z} > y ({y}) ? → {'SÍ' if x + z > y else 'NO'}")
    print(f"  y + z = {y} + {z} = {y + z} > x ({x}) ? → {'SÍ' if y + z > x else 'NO'}")
    print()
    print("Para que sea triángulo, deben cumplirse TODAS las desigualdades.")