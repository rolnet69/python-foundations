import os
import csv
from infrastructure.csv_repositories import (
    CSVUserRepository, CSVProductRepository, 
    CSVCategoryRepository, CSVInvoiceRepository
)
from application.user_service import UserService
from application.product_service import ProductService
from application.invoice_service import InvoiceService
from application.category_service import CategoryService
from interface_adapters.menu import Menu

def verificar_archivos_ia():
    """Verifica que los archivos generados para pruebas existen"""
    archivos_necesarios = ['usuarios.csv', 'categorias.csv', 'productos.csv']
    carpeta = 'data'
    
    print("\n" + "="*60)
    print(" VERIFICANDO DATOS GENERADOS PARA PRUEBAS ".center(60, "="))
    print("="*60)
    
    todos_existen = True
    for archivo in archivos_necesarios:
        ruta = os.path.join(carpeta, archivo)
        if os.path.exists(ruta):
            print(f"✅ {archivo} encontrado")
        else:
            print(f"❌ {archivo} NO encontrado")
            todos_existen = False
    
    return todos_existen

def mostrar_info_ia():
    """Muestra información de los archivos generados para pruebas"""
    print("\n" + "="*60)
    print(" DATOS GENERADOS POR INTELIGENCIA ARTIFICIAL ".center(60, "="))
    print("="*60)
    
    # Mostrar usuarios
    with open('data/usuarios.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print("\n👤 USUARIOS:")
        print("-" * 40)
        for row in reader:
            print(f"   {row['nombres']} {row['apellidos']}")
            print(f"   Usuario: {row['username']} | Contraseña: {row['password']} | Rol: {row['role']}")
            print()
    
    # Mostrar categorías
    with open('data/categorias.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print("\n📚 CATEGORÍAS:")
        print("-" * 40)
        categorias = []
        for row in reader:
            categorias.append(row['nombre'])
        print(f"   {', '.join(categorias)}")
        print(f"   Total: {len(categorias)} categorías")
    
    # Mostrar productos
    with open('data/productos.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print("\n📦 PRODUCTOS:")
        print("-" * 40)
        total = 0
        agotados = 0
        print(f"{'ID':<5} {'NOMBRE':<30} {'PRECIO':<8} {'STOCK':<6} {'CATEGORÍA'}")
        print("-" * 70)
        for row in reader:
            total += 1
            stock = int(row['stock'])
            if stock == 0:
                agotados += 1
            print(f"{row['id']:<5} {row['nombre'][:28]:<30} ${row['precio']:<7} {row['stock']:<6} {row['categoria']}")
        print("-" * 70)
        print(f"Total: {total} productos | Agotados: {agotados}")

def seed_data():
    """Función vacía porque los datos ya vienen de la IA"""
    pass

def main():
    # Crear directorio data si no existe
    os.makedirs("data", exist_ok=True)
    
    # Verificar archivos generados para pruebas
    if not verificar_archivos_ia():
        print("\n" + "="*60)
        print(" ERROR: FALTAN ARCHIVOS GENERADOS PARA PRUEBAS ".center(60, "="))
        print("="*60)
        print("\nPara generar los datos:")
        print("1. Pide a ChatGPT u otra IA que genere los archivos CSV")
        print("2. Guarda los archivos en la carpeta 'data/'")
        print("3. Vuelve a ejecutar el programa")
        print("\nArchivos necesarios:")
        print("   - usuarios.csv")
        print("   - categorias.csv")
        print("   - productos.csv")
        input("\nPresione Enter para salir...")
        return
    
    # Mostrar información de los datos generados para pruebas
    mostrar_info_ia()
    
    print("\n" + "="*60)
    input("Presione Enter para continuar al menú principal...")
    
    # Inicializar repositorios
    user_repo = CSVUserRepository()
    product_repo = CSVProductRepository()
    category_repo = CSVCategoryRepository()
    invoice_repo = CSVInvoiceRepository()
    
    # Inicializar servicios
    user_service = UserService(user_repo)
    product_service = ProductService(product_repo, category_repo)
    invoice_service = InvoiceService(invoice_repo, product_repo)
    category_service = CategoryService(category_repo)
    
    # Iniciar menú
    menu = Menu(user_service, product_service, invoice_service, category_service)
    menu.main_menu()

if __name__ == "__main__":
    main()