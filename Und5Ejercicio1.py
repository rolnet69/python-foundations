class Persona:
    def __init__(self, nombres, apellidos, edad):
        self.nombres = nombres
        self.apellidos = apellidos
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self.edad = edad
    
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}".strip()
    
    def __str__(self):
        return f"{self.nombre_completo()} ({self.edad} años)"


# PROGRAMA PRINCIPAL
print("Registro de personas")
print("-" * 30)

personas = []
while True:
    print(f"\nPersona #{len(personas) + 1}:")
    nombres = input("Ingrese Nombres: ").strip()
    if not nombres:
        break
    
    apellidos = input("Ingrese Apellidos: ").strip()
    
    # Validar edad
    try:
        edad = int(input("Ingrese Edad: "))
        if edad < 0:
            print("La edad no puede ser negativa")
            continue
    except ValueError:
        print("Ingresa un número válido")
        continue
    
    personas.append(Persona(nombres, apellidos, edad))

print("\n" + "=" * 40)
print("Personas registradas")
print("=" * 40)

for i, p in enumerate(personas, 1):
    print(f"{i}. {p}")