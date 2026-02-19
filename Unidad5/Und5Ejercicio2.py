class Estudiante:
    
    def __init__(self, carnet, nombres, apellidos, carrera):
        self.carnet = carnet
        self.nombres = nombres
        self.apellidos = apellidos
        self.carrera = carrera
    
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}".strip()
    
    def __str__(self):
        return f"{self.carnet} | {self.nombre_completo()} | {self.carrera}"
    
    def __repr__(self):
        return f"Estudiante('{self.carnet}', '{self.nombres}', '{self.apellidos}', '{self.carrera}')"


def cargar_estudiantes_desde_archivo(nombre_archivo):

    estudiantes = []
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            
            # La primera línea es la cabecera, la saltamos
            for i, linea in enumerate(lineas[1:], 2):  # i empieza en 2 por la cabecera
                linea = linea.strip()
                if not linea:
                    continue
                
                # Separar por comas
                partes = linea.split(',')
                
                if len(partes) < 4:
                    print(f"Línea {i} ignorada: formato incorrecto - {linea}")
                    continue
                
                carnet = partes[0].strip()
                nombres = partes[1].strip()
                apellidos = partes[2].strip()
                carrera = partes[3].strip()
                
                # Crear instancia y agregar a la lista
                estudiante = Estudiante(carnet, nombres, apellidos, carrera)
                estudiantes.append(estudiante)
        
        print("=" * 90)
        print(f"Archivo leído correctamente: {len(estudiantes)} estudiantes cargados.")
        print("=" * 90)
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'")
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    return estudiantes


def mostrar_estudiantes(estudiantes, cantidad=None):
    if not estudiantes:
        print("No hay estudiantes para mostrar.")
        return
    
    mostrar = estudiantes if cantidad is None else estudiantes[:cantidad]
    

    print(f"{'#':<3} {'Carnet':<10} {'Nombres':<20} {'Apellidos':<20} {'Carrera':<30}")
    print("-" * 90)
    
    for i, est in enumerate(mostrar, 1):
        print(f"{i:<3} {est.carnet:<10} {est.nombres:<20} {est.apellidos:<20} {est.carrera:<30}")
    

# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    
    # Nombre del archivo
    archivo = "estudiantes_practica.txt"
    
    # Cargar estudiantes
    lista_estudiantes = cargar_estudiantes_desde_archivo(archivo)
    
    if lista_estudiantes:
        # Mostrar todos
        mostrar_estudiantes(lista_estudiantes)
        
      
    print("\n" + "=" * 90)