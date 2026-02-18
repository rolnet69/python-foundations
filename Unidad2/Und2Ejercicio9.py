# Programa que recibe una entrada e imprime únicamente si es de tipo entero
entrada = input("Ingrese un valor: ")

# Intentar convertir a entero
try:
    numero = int(entrada)
    print(f"La entrada es un número entero: {numero}")
except ValueError:
    # No hacer nada si no es un entero
    pass

# Siempre imprimir al finalizar
print("Fin de la ejecución")