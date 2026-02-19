import csv
import os

class Usuario:
    def __init__(self, carnet, nombres, apellidos, facultad, tipo):
        self.carnet = carnet
        self.nombres = nombres
        self.apellidos = apellidos
        self.facultad = facultad
        self.tipo = tipo


def guardar_usuario(usuario):
    with open('usuarios.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([usuario.carnet, usuario.nombres, usuario.apellidos, usuario.tipo, usuario.facultad])
    print(f"{usuario.tipo} guardado: {usuario.carnet}")


def crear_archivo_si_no_existe():
    if not os.path.exists('usuarios.csv'):
        with open('usuarios.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Carnet', 'Nombres', 'Apellidos', 'Tipo', 'Facultad'])


def listar_usuarios():
    try:
        with open('usuarios.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            datos = list(reader)
        
        if len(datos) <= 1:
            print("\nNo hay usuarios registrados.")
            return
        
        print("\n" + "=" * 100)
        print("LISTA DE USUARIOS".center(100))
        print("=" * 100)
        
        # Cabecera
        print(f"{'#':<4} {datos[0][0]:<12} {datos[0][1]:<20} {datos[0][2]:<20} {datos[0][3]:<12} {datos[0][4]:<25}")
        print("-" * 100)
        
        # Datos
        for i, fila in enumerate(datos[1:], 1):
            print(f"{i:<4} {fila[0]:<12} {fila[1]:<20} {fila[2]:<20} {fila[3]:<12} {fila[4]:<25}")
        
        print("=" * 100)
        print(f"Total: {len(datos)-1} usuarios")
        print("=" * 100)
        
    except Exception as e:
        print(f"Error: {e}")


# Programa principal
crear_archivo_si_no_existe()

while True:
    print("\n" + "=" * 40)
    print("MENÚ PRINCIPAL")
    print("=" * 40)
    print("1. Registrar Estudiante")
    print("2. Registrar Profesor")
    print("3. Listar usuarios")
    print("4. Salir")
    print("-" * 40)
    
    op = input("Opción: ").strip()
    
    if op == "1":
        print("\nNUEVO ESTUDIANTE")
        print("-" * 30)
        u = Usuario(
            input("Carnet: ").strip(),
            input("Nombres: ").strip(),
            input("Apellidos: ").strip(),
            input("Facultad: ").strip(),
            "Estudiante"
        )
        guardar_usuario(u)
    
    elif op == "2":
        print("\nNUEVO PROFESOR")
        print("-" * 30)
        u = Usuario(
            input("Carnet: ").strip(),
            input("Nombres: ").strip(),
            input("Apellidos: ").strip(),
            input("Facultad: ").strip(),
            "Profesor"
        )
        guardar_usuario(u)
    
    elif op == "3":
        listar_usuarios()
    
    elif op == "4":
        print("\n¡Hasta luego!")
        break
    
    else:
        print("Opción no válida")