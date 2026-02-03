print("--------------------------------------------------------")
print("Ejercicio 8")
print("--------------------------------------------------------")

# Solicitar número con validación y reintento
numeroValido = False
while not numeroValido:
    numero = input("Ingresa un número entero positivo: ").strip()
    
    if (numero.isdigit() and int(numero) > 0 and 
        (len(numero) == 1 or numero[0] != '0')):
        numeroValido = True
    else:
        print("ERROR: Número entero positivo válido requerido.")
        print("       Intenta nuevamente.\n")

numDigitos = len(numero)
suma = 0

for digito in numero:
    suma += int(digito) ** numDigitos

numeroInt = int(numero)

print(f"\nNúmero ingresado: {numeroInt}")
print(f"Cantidad de dígitos: {numDigitos}")

print("Cálculo: ", end="")
for i, digito in enumerate(numero):
    if i > 0:
        print(" + ", end="")
    print(f"{digito}^{numDigitos}", end="")
print(f" = {suma}")

if suma == numeroInt:
    print(f"\n{numeroInt} ES un Número Narcisista")
else:
    print(f"\n{numeroInt} NO es un Número Narcisista")