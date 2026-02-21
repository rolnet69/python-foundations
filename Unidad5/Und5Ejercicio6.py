import os

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')


class Vehiculo:
    """Clase base para vehículos."""
    
    def __init__(self, marca, modelo, tarifa_diaria):
        self._marca = marca
        self._modelo = modelo
        self._tarifa_diaria = float(tarifa_diaria)
    
    @property
    def marca(self):
        return self._marca
    
    @property
    def modelo(self):
        return self._modelo
    
    @property
    def tarifa_diaria(self):
        return self._tarifa_diaria
    
    def calcular_alquiler(self, dias):
        """Calcula el costo de alquiler base (tarifa * días)."""
        if dias <= 0:
            return 0
        return self._tarifa_diaria * dias
    
    def informacion(self):
        """Retorna la información básica del vehículo."""
        return f"{self._marca} {self._modelo} | Tarifa: ${self._tarifa_diaria:.2f}/día"
    
    def __str__(self):
        return self.informacion()


class Auto(Vehiculo):
    """Clase para autos particulares."""
    
    def __init__(self, marca, modelo, tarifa_diaria, puertas):
        super().__init__(marca, modelo, tarifa_diaria)
        self._puertas = puertas
    
    @property
    def puertas(self):
        return self._puertas
    
    def calcular_alquiler(self, dias):
        """El auto no tiene cargos extras."""
        return super().calcular_alquiler(dias)
    
    def informacion(self):
        return f"AUTO: {super().informacion()} | {self._puertas} puertas"
    
    def __str__(self):
        return self.informacion()


class Camioneta(Vehiculo):
    """Clase para camionetas de carga."""
    
    CARGO_SEGURO = 10.0
    
    def __init__(self, marca, modelo, tarifa_diaria):
        super().__init__(marca, modelo, tarifa_diaria)
    
    def calcular_alquiler(self, dias):
        """La camioneta tiene un cargo fijo de seguro de carga."""
        base = super().calcular_alquiler(dias)
        if base == 0:
            return 0
        return base + self.CARGO_SEGURO
    
    def informacion(self):
        return f"CAMIONETA: {super().informacion()} | Seguro: ${self.CARGO_SEGURO:.2f}"
    
    def __str__(self):
        return self.informacion()


class Flota:
    """Clase para gestionar la flota de vehículos."""
    
    def __init__(self):
        self._vehiculos = []
    
    def agregar_vehiculo(self, vehiculo):
        """Agrega un vehículo a la flota."""
        self._vehiculos.append(vehiculo)
        print(f"{vehiculo.informacion()} agregado a la flota.")
    
    def listar_vehiculos(self):
        """Muestra todos los vehículos de la flota."""
        if not self._vehiculos:
            print("\n📭 No hay vehículos en la flota.")
            return
        
        print("\n" + "=" * 80)
        print("FLOTA DE VEHÍCULOS FASTCODE".center(80))
        print("=" * 80)
        print(f"{'#':<3} {'TIPO':<12} {'VEHÍCULO':<35} {'TARIFA':<12} {'EXTRAS':<15}")
        print("-" * 80)
        
        for i, v in enumerate(self._vehiculos, 1):
            if isinstance(v, Auto):
                tipo = "Auto"
                extras = f"{v.puertas} puertas"
            else:
                tipo = "Camioneta"
                extras = f"Seguro ${Camioneta.CARGO_SEGURO}"
            
            vehiculo_str = f"{v.marca} {v.modelo}"
            print(f"{i:<3} {tipo:<12} {vehiculo_str:<35} ${v.tarifa_diaria:<10.2f} {extras:<15}")
        
        print("=" * 80)
    
    def buscar_por_marca(self, marca):
        """Busca vehículos por marca."""
        resultados = [v for v in self._vehiculos if v.marca.lower() == marca.lower()]
        
        if not resultados:
            print(f"\nNo se encontraron vehículos de marca '{marca}'.")
            return
        
        print(f"\nVEHÍCULOS MARCA '{marca.upper()}':")
        print("-" * 60)
        for v in resultados:
            print(f"  • {v.informacion()}")
    
    def simular_alquiler(self, indice, dias):
        """Simula el alquiler de un vehículo por ciertos días."""
        if indice < 1 or indice > len(self._vehiculos):
            print("Índice de vehículo no válido.")
            return
        
        v = self._vehiculos[indice - 1]
        costo = v.calcular_alquiler(dias)
        
        print(f"\nSIMULACIÓN DE ALQUILER:")
        print("-" * 50)
        print(f"Vehículo: {v.informacion()}")
        print(f"Días: {dias}")
        print(f"Costo total: ${costo:.2f}")
        if isinstance(v, Camioneta):
            print(f"(Incluye seguro de carga: ${Camioneta.CARGO_SEGURO:.2f})")


def validar_entero_positivo(mensaje):
    """Valida que la entrada sea un entero positivo."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("El valor debe ser positivo.")
        except ValueError:
            print("Ingresa un número entero válido.")


def validar_float_positivo(mensaje):
    """Valida que la entrada sea un número positivo."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("El valor debe ser positivo.")
        except ValueError:
            print("Ingresa un número válido.")


def menu_principal():
    """Muestra el menú principal del sistema."""
    flota = Flota()
    
    # Agregar algunos vehículos de ejemplo
    flota.agregar_vehiculo(Auto("Toyota", "Corolla", 45.0, 4))
    flota.agregar_vehiculo(Auto("Honda", "Civic", 50.0, 4))
    flota.agregar_vehiculo(Camioneta("Ford", "Ranger", 75.0))
    flota.agregar_vehiculo(Camioneta("Chevrolet", "S10", 80.0))
    
    while True:
        limpiar_pantalla()
        print("\n" + "=" * 60)
        print("SISTEMA DE ALQUILER FASTCODE".center(60))
        print("=" * 60)
        print("1. Listar flota de vehículos")
        print("2. Agregar auto particular")
        print("3. Agregar camioneta de carga")
        print("4. Simular alquiler")
        print("5. Buscar por marca")
        print("6. Salir")
        print("-" * 60)
        
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1":
            flota.listar_vehiculos()
            input("\nPresiona Enter para continuar...")
        
        elif opcion == "2":
            limpiar_pantalla()
            print("\n" + "=" * 40)
            print("AGREGAR AUTO PARTICULAR")
            print("=" * 40)
            marca = input("Marca: ").strip()
            modelo = input("Modelo: ").strip()
            tarifa = validar_float_positivo("Tarifa diaria ($): ")
            puertas = validar_entero_positivo("Número de puertas: ")
            
            auto = Auto(marca, modelo, tarifa, puertas)
            flota.agregar_vehiculo(auto)
            input("\nPresiona Enter para continuar...")
        
        elif opcion == "3":
            limpiar_pantalla()
            print("\n" + "=" * 40)
            print("AGREGAR CAMIONETA DE CARGA")
            print("=" * 40)
            marca = input("Marca: ").strip()
            modelo = input("Modelo: ").strip()
            tarifa = validar_float_positivo("Tarifa diaria ($): ")
            
            camioneta = Camioneta(marca, modelo, tarifa)
            flota.agregar_vehiculo(camioneta)
            input("\nPresiona Enter para continuar...")
        
        elif opcion == "4":
            limpiar_pantalla()
            print("\n" + "=" * 40)
            print("SIMULAR ALQUILER")
            print("=" * 40)
            
            flota.listar_vehiculos()
            
            if flota._vehiculos:
                try:
                    indice = int(input("\nNúmero del vehículo a alquilar: "))
                    dias = validar_entero_positivo("Cantidad de días: ")
                    flota.simular_alquiler(indice, dias)
                except ValueError:
                    print("Índice no válido.")
            
            input("\nPresiona Enter para continuar...")
        
        elif opcion == "5":
            limpiar_pantalla()
            print("\n" + "=" * 40)
            print("BUSCAR POR MARCA")
            print("=" * 40)
            marca = input("Marca a buscar: ").strip()
            flota.buscar_por_marca(marca)
            input("\nPresiona Enter para continuar...")
        
        elif opcion == "6":
            limpiar_pantalla()
            print("\n¡Gracias por usar FastCode!")
            break
        
        else:
            input("Opción no válida. Presiona Enter para continuar...")


if __name__ == "__main__":
    menu_principal()