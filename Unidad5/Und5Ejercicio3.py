class Date:
   
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
    
    def rellenar_con_ceros(self, numero, cifras):
        num_str = str(numero)
        return '0' * (cifras - len(num_str)) + num_str
    
    def __str__(self):
        # Formatear día y mes (siempre 2 cifras)
        dia_formateado = self.rellenar_con_ceros(self.dia, 2)
        mes_formateado = self.rellenar_con_ceros(self.mes, 2)
        
        # Formatear año según las reglas:
        # - Menor a 1000: 1 cero delante (4 cifras total)
        # - Menor a 100: 2 ceros delante (4 cifras total)
        # - Menor a 10: 3 ceros delante (4 cifras total)
        # - Mayor o igual a 1000: sin ceros adicionales
        if self.año < 10:
            año_formateado = self.rellenar_con_ceros(self.año, 4)
        elif self.año < 100:
            año_formateado = self.rellenar_con_ceros(self.año, 4)
        elif self.año < 1000:
            año_formateado = self.rellenar_con_ceros(self.año, 4)
        else:
            año_formateado = str(self.año)
        
        return f"{dia_formateado}/{mes_formateado}/{año_formateado}"

def validar_dia():
    while True:
        try:
            dia = int(input("Día: "))
            if 1 <= dia <= 31:
                return dia
            else:
                print("El día debe estar entre 1 y 31")
        except ValueError:
            print("Ingresa un número válido")


def validar_mes():
    while True:
        try:
            mes = int(input("Mes: "))
            if 1 <= mes <= 12:
                return mes
            else:
                print("El mes debe estar entre 1 y 12")
        except ValueError:
            print("Ingresa un número válido")


def validar_año():
    while True:
        try:
            año = int(input("Año: "))
            if año >= 0:
                return año
            else:
                print("El año debe ser un número positivo")
        except ValueError:
            print("Ingresa un número válido")

# PROGRAMA PRINCIPAL
print("=" * 50)
print("Date: dia, mes y año.")

# Entrada de usuario
print("Ingresa una fecha por partes (Dia, Mes, Año)")
print("=" * 50)

try:
    dia = validar_dia()
    mes = validar_mes()
    año = validar_año()
    
    fecha_usuario = Date(dia, mes, año)
    print(f"\nFecha con formato dd/mm/yyyy: {fecha_usuario}")
    
except ValueError:
    print("Error: Ingresa valores numéricos válidos")

print("\n" + "=" * 50)