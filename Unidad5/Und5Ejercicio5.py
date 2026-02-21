import csv
import os
from getpass import getpass

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Usuario:
    """Clase que representa un usuario del sistema de ahorros."""
    
    def __init__(self, username, password, nombre, saldo=0.0):
        self._username = username
        self._password = password  
        self._nombre = nombre
        self._saldo = float(saldo)
    
    # Getters
    @property
    def username(self):
        return self._username
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def saldo(self):
        return self._saldo
    
    def verificar_password(self, password):
        return self._password == password
    
    def depositar(self, monto):
        """Realiza un depósito en la cuenta."""
        if monto > 0:
            self._saldo += monto
            return True, f"Depósito exitoso. Nuevo saldo: ${self._saldo:.2f}"
        return False, "El monto debe ser positivo"
    
    def retirar(self, monto):
        """Realiza un retiro si hay fondos suficientes."""
        if monto <= 0:
            return False, "El monto debe ser positivo"
        if monto > self._saldo:
            return False, f"Fondos insuficientes. Saldo actual: ${self._saldo:.2f}"
        
        self._saldo -= monto
        return True, f"Retiro exitoso. Nuevo saldo: ${self._saldo:.2f}"
    
    def to_list(self):
        return [self._username, self._password, self._nombre, str(self._saldo)]
    
    def __str__(self):
        return f"{self._nombre} (@{self._username}) - Saldo: ${self._saldo:.2f}"


class SistemaAhorros:
    
    def __init__(self, archivo="usuarios.csv"):
        self._archivo = archivo
        self._usuarios = {}  
        self._usuario_actual = None
        self._crear_archivo_si_no_existe()
        self._cargar_usuarios()
    
    def _crear_archivo_si_no_existe(self):
        if not os.path.exists(self._archivo):
            with open(self._archivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['USERNAME', 'PASSWORD', 'NOMBRE', 'SALDO'])
    
    def _cargar_usuarios(self):
        try:
            with open(self._archivo, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  
                for fila in reader:
                    if len(fila) >= 4:
                        username, password, nombre, saldo = fila
                        self._usuarios[username] = Usuario(username, password, nombre, saldo)
        except Exception as e:
            print(f"Error al cargar usuarios: {e}")
    
    def _guardar_usuario(self, usuario):
        """Guarda un nuevo usuario en el archivo."""
        with open(self._archivo, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(usuario.to_list())
    
    def _actualizar_archivo(self):
        """Reescribe todo el archivo con los datos actualizados."""
        with open(self._archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['USERNAME', 'PASSWORD', 'NOMBRE', 'SALDO'])
            for usuario in self._usuarios.values():
                writer.writerow(usuario.to_list())
    
    def registrar_usuario(self):
        """Registra un nuevo usuario en el sistema."""
        limpiar_pantalla()
        print("\n" + "=" * 40)
        print("REGISTRO DE NUEVO USUARIO")
        print("=" * 40)
        
        username = input("Username: ").strip()
        if username in self._usuarios:
            input("El username ya existe. Intenta con otro.\nPresiona Enter para continuar...")
            return False
        
        password = getpass("Contraseña: ").strip()
        if not password:
            input("La contraseña no puede estar vacía.\nPresiona Enter para continuar...")
            return False
        
        nombre = input("Nombre completo: ").strip()
        if not nombre:
            input("El nombre no puede estar vacío.\nPresiona Enter para continuar...")
            return False
        
        usuario = Usuario(username, password, nombre)
        self._usuarios[username] = usuario
        self._guardar_usuario(usuario)
        input(f"Usuario registrado exitosamente. ¡Bienvenido, {nombre}!\nPresiona Enter para continuar...")
        return True
    
    def iniciar_sesion(self):
        """Inicia sesión de un usuario existente."""
        limpiar_pantalla()
        print("\n" + "=" * 40)
        print("INICIAR SESIÓN")
        print("=" * 40)
        
        username = input("Username: ").strip()
        if username not in self._usuarios:
            input("Usuario no encontrado.\nPresiona Enter para continuar...")
            return False
        
        password = getpass("Contraseña: ").strip()
        usuario = self._usuarios[username]
        
        if not usuario.verificar_password(password):
            input("Contraseña incorrecta.\nPresiona Enter para continuar...")
            return False
        
        self._usuario_actual = usuario
        limpiar_pantalla()
        print(f"¡Bienvenido, {usuario.nombre}!")
        input("Presiona Enter para continuar...")
        return True
    
    def menu_principal(self):
        """Muestra el menú principal del sistema."""
        while True:
            limpiar_pantalla()
            print("\n" + "=" * 50)
            print("SISTEMA DE AHORROS".center(50))
            print("=" * 50)
            print("1. Iniciar sesión")
            print("2. Registrar nuevo usuario")
            print("3. Salir")
            print("-" * 50)
            
            opcion = input("Selecciona una opción: ").strip()
            
            if opcion == "1":
                if self.iniciar_sesion():
                    self.menu_usuario()
            elif opcion == "2":
                self.registrar_usuario()
            elif opcion == "3":
                limpiar_pantalla()
                print("\n¡Hasta luego!")
                break
            else:
                input("Opción no válida.\nPresiona Enter para continuar...")
    
    def menu_usuario(self):
        """Muestra el menú para un usuario autenticado."""
        while self._usuario_actual:
            limpiar_pantalla()
            print("\n" + "=" * 50)
            print(f"BIENVENIDO, {self._usuario_actual.nombre.upper()}".center(50))
            print("=" * 50)
            print(f"Saldo actual: ${self._usuario_actual.saldo:.2f}")
            print("-" * 50)
            print("1. Depositar")
            print("2. Retirar")
            print("3. Ver saldo")
            print("4. Cerrar sesión")
            print("-" * 50)
            
            opcion = input("Selecciona una opción: ").strip()
            
            if opcion == "1":
                self._depositar()
            elif opcion == "2":
                self._retirar()
            elif opcion == "3":
                print(f"\nSaldo actual: ${self._usuario_actual.saldo:.2f}")
                input("\nPresiona Enter para continuar...")
            elif opcion == "4":
                self._usuario_actual = None
                limpiar_pantalla()
                input("Sesión cerrada.\nPresiona Enter para continuar...")
            else:
                input("Opción no válida.\nPresiona Enter para continuar...")
    
    def _depositar(self):
        """Procesa un depósito."""
        limpiar_pantalla()
        print("\n" + "=" * 40)
        print("DEPOSITAR".center(40))
        print("=" * 40)
        print(f"Saldo actual: ${self._usuario_actual.saldo:.2f}")
        print("-" * 40)
        
        try:
            monto = float(input("Monto a depositar: $"))
            exito, mensaje = self._usuario_actual.depositar(monto)
            print(f"\n{mensaje}")
            if exito:
                self._actualizar_archivo()
            input("\nPresiona Enter para continuar...")
        except ValueError:
            input("Ingresa un monto válido.\nPresiona Enter para continuar...")
    
    def _retirar(self):
        """Procesa un retiro."""
        limpiar_pantalla()
        print("\n" + "=" * 40)
        print("RETIRAR".center(40))
        print("=" * 40)
        print(f"Saldo actual: ${self._usuario_actual.saldo:.2f}")
        print("-" * 40)
        
        try:
            monto = float(input("Monto a retirar: $"))
            exito, mensaje = self._usuario_actual.retirar(monto)
            print(f"\n{mensaje}")
            if exito:
                self._actualizar_archivo()
            input("\nPresiona Enter para continuar...")
        except ValueError:
            input("Ingresa un monto válido.\nPresiona Enter para continuar...")


if __name__ == "__main__":
    sistema = SistemaAhorros()
    sistema.menu_principal()