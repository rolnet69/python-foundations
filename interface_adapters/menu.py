import os
import time

class Menu:
    def __init__(self, user_service, product_service, invoice_service, category_service):
        self.user_service = user_service
        self.product_service = product_service
        self.invoice_service = invoice_service
        self.category_service = category_service
        self.current_user = None
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self, title: str):
        print("=" * 60)
        print(f"{title:^60}")
        print("=" * 60)
    
    def print_success(self, message: str):
        print(f"✅ {message}")
    
    def print_error(self, message: str):
        print(f"❌ {message}")
    
    def print_info(self, message: str):
        print(f"ℹ️ {message}")
    
    def input_with_validation(self, prompt: str, required: bool = True, allow_exit: bool = True):
        while True:
            value = input(prompt).strip()
            if allow_exit and value.lower() == 'salir':
                return 'salir'
            if required and not value:
                self.print_error("Este campo no puede estar vacío")
            else:
                return value
    
    def get_greeting(self, nombre_usuario):
        """Saludo personalizado según la hora del día"""
        hora = time.localtime().tm_hour
        
        if hora < 12:
            return f"🌅 ¡Buenos días, {nombre_usuario}!"
        elif hora < 18:
            return f"☀️ ¡Buenas tardes, {nombre_usuario}!"
        else:
            return f"🌙 ¡Buenas noches, {nombre_usuario}!"
    
    def main_menu(self):
        while True:
            self.clear_screen()
            self.print_header("🏪 SISTEMA DE SUPERMERCADO")
            print("\n1. Iniciar sesión")
            print("2. Salir")
            
            option = input("\nSeleccione una opción: ").strip()
            
            if option == "1":
                self.login()
            elif option == "2":
                self.print_info("¡Hasta luego!")
                break
            else:
                self.print_error("Opción inválida")
                input("\nPresione Enter para continuar...")
    
    def login(self):
        self.clear_screen()
        self.print_header("🔐 INICIAR SESIÓN")
        self.print_info("(Escriba 'salir' para cancelar)")
        
        while True:
            username = self.input_with_validation("Usuario: ")
            if username == 'salir':
                return
            
            password = self.input_with_validation("Contraseña: ")
            if password == 'salir':
                return
            
            success, user, message = self.user_service.login(username, password)
            
            if success:
                self.current_user = user
                nombre = user.nombres.split()[0]  
                saludo = self.get_greeting(nombre)
                self.print_success(saludo)
                input("\nPresione Enter para continuar...")
                
                if user.role == "Administrador":
                    self.admin_menu()
                else:
                    self.check_first_login()
                break
            else:
                self.print_error(message)
                retry = input("\n¿Intentar nuevamente? (s/n): ").lower()
                if retry != 's':
                    break
    
    def check_first_login(self):
        if self.current_user.first_login:
            self.change_password(first_login=True)
        else:
            self.client_menu()
    
    def change_password(self, first_login: bool = False):
        self.clear_screen()
        self.print_header("🔑 CAMBIAR CONTRASEÑA")
        self.print_info("(Escriba 'salir' para cancelar)")
        
        if first_login:
            self.print_info("Es su primer inicio de sesión. Debe cambiar su contraseña.")
        
        while True:
            new_password = self.input_with_validation("Nueva contraseña: ")
            if new_password == 'salir':
                self.print_info("Operación cancelada")
                input("\nPresione Enter para continuar...")
                if first_login:
                    return
                break
            
            confirm_password = self.input_with_validation("Confirmar contraseña: ")
            if confirm_password == 'salir':
                self.print_info("Operación cancelada")
                input("\nPresione Enter para continuar...")
                if first_login:
                    return
                break
            
            success, message = self.user_service.change_password(
                self.current_user, new_password, confirm_password
            )
            
            if success:
                self.print_success(message)
                input("\nPresione Enter para continuar...")
                if first_login:
                    self.client_menu()
                break
            else:
                self.print_error(message)
    
    def admin_menu(self):
        while True:
            self.clear_screen()
            nombre = self.current_user.nombres.split()[0]
            saludo = self.get_greeting(nombre)
            self.print_header(f"👑 {saludo}")
            print("\n1. Crear usuario")
            print("2. Gestionar productos")
            print("3. Gestionar categorías")
            print("4. Ver informe de productos")
            print("5. Resetear contraseña de cliente")
            print("6. Cerrar sesión")
            
            option = input("\nSeleccione una opción: ").strip()
            
            if option == "1":
                self.create_user()
            elif option == "2":
                self.manage_products()
            elif option == "3":
                self.manage_categories()
            elif option == "4":
                self.view_inventory_report()
            elif option == "5":
                self.reset_user_password()
            elif option == "6":
                self.current_user = None
                break
            else:
                self.print_error("Opción inválida")
                input("\nPresione Enter para continuar...")
    
    def create_user(self):
        self.clear_screen()
        self.print_header("👤 CREAR NUEVO USUARIO")
        self.print_info("(Escriba 'salir' en cualquier campo para cancelar)")
        
        nombres = self.input_with_validation("Nombres: ")
        if nombres == 'salir':
            self.print_info("Operación cancelada")
            input("\nPresione Enter para continuar...")
            return
        
        apellidos = self.input_with_validation("Apellidos: ")
        if apellidos == 'salir':
            self.print_info("Operación cancelada")
            input("\nPresione Enter para continuar...")
            return
        
        password = self.input_with_validation("Contraseña inicial: ")
        if password == 'salir':
            self.print_info("Operación cancelada")
            input("\nPresione Enter para continuar...")
            return
        
        print("\nRoles disponibles:")
        print("1. Administrador")
        print("2. Cliente")
        print("0. Cancelar")
        
        role_option = input("Seleccione rol (0-2): ").strip()
        if role_option == '0':
            self.print_info("Operación cancelada")
            input("\nPresione Enter para continuar...")
            return
        
        role = "Administrador" if role_option == "1" else "Cliente"
        
        success, message = self.user_service.create_user(
            nombres, apellidos, password, role
        )
        
        if success:
            self.print_success(message)
        else:
            self.print_error(message)
        
        input("\nPresione Enter para continuar...")
    
    def reset_user_password(self):
        self.clear_screen()
        self.print_header("🔄 RESETEAR CONTRASEÑA DE CLIENTE")
        self.print_info("(Escriba 'salir' para cancelar)")
        
        # Mostrar lista de clientes
        users = self.user_service.user_repository.get_all()
        clientes = []
        for u in users:
            if u.role == "Cliente":
                clientes.append(u)
        
        if not clientes:
            self.print_info("No hay clientes registrados")
            input("\nPresione Enter para continuar...")
            return
        
        print("\n📋 CLIENTES REGISTRADOS:")
        for i, cliente in enumerate(clientes, 1):
            print(f"   {i}. {cliente.nombres} {cliente.apellidos} - {cliente.username}")
        
        print("\nOpciones:")
        print("   1. Buscar por username")
        print("   2. Seleccionar de la lista")
        print("   0. Cancelar")
        
        option = input("\nSeleccione opción: ").strip()
        
        username = None
        
        if option == "1":
            username = self.input_with_validation("Ingrese username del cliente: ")
            if username == 'salir':
                return
            
            # Verificar que existe y es cliente
            user = self.user_service.user_repository.get_by_username(username)
            if not user or user.role != "Cliente":
                self.print_error("Cliente no encontrado")
                input("\nPresione Enter para continuar...")
                return
        
        elif option == "2":
            try:
                idx = int(input("Seleccione número de cliente: ")) - 1
                if 0 <= idx < len(clientes):
                    username = clientes[idx].username
                else:
                    self.print_error("Opción inválida")
                    input("\nPresione Enter para continuar...")
                    return
            except ValueError:
                self.print_error("Ingrese un número válido")
                input("\nPresione Enter para continuar...")
                return
        else:
            return
        
        # Confirmar y resetear contraseña
        print(f"\nCliente seleccionado: {username}")
        new_password = self.input_with_validation("Nueva contraseña temporal: ")
        if new_password == 'salir':
            return
        
        confirm = input(f"¿Resetear contraseña de {username} a '{new_password}'? (s/n): ")
        
        if confirm.lower() == 's':
            success, message = self.user_service.reset_user_password(username, new_password)
            if success:
                self.print_success(message)
                self.print_info("El cliente deberá cambiar esta contraseña en su próximo ingreso.")
            else:
                self.print_error(message)
        else:
            self.print_info("Operación cancelada")
        
        input("\nPresione Enter para continuar...")
    
    def manage_products(self):
        while True:
            self.clear_screen()
            self.print_header("📦 GESTIÓN DE PRODUCTOS")
            print("\n1. Agregar producto")
            print("2. Actualizar producto")
            print("3. Eliminar producto")
            print("4. Listar productos")
            print("5. Volver")
            
            option = input("\nSeleccione una opción: ").strip()
            
            if option == "1":
                self.add_product()
            elif option == "2":
                self.update_product()
            elif option == "3":
                self.delete_product()
            elif option == "4":
                self.list_products(simple=False)
            elif option == "5":
                break
            else:
                self.print_error("Opción inválida")
                input("\nPresione Enter para continuar...")
    
    def add_product(self):
        self.clear_screen()
        self.print_header("➕ AGREGAR PRODUCTO")
        self.print_info("(Escriba 'salir' para cancelar)")
        
        nombre = self.input_with_validation("Nombre del producto: ")
        if nombre == 'salir':
            self.print_info("Operación cancelada")
            input("\nPresione Enter para continuar...")
            return
        
        while True:
            try:
                precio_input = self.input_with_validation("Precio: $")
                if precio_input == 'salir':
                    self.print_info("Operación cancelada")
                    input("\nPresione Enter para continuar...")
                    return
                precio = float(precio_input)
                if precio > 0:
                    break
                self.print_error("El precio debe ser mayor que 0")
            except ValueError:
                self.print_error("Ingrese un número válido")
        
        while True:
            try:
                stock_input = self.input_with_validation("Stock: ")
                if stock_input == 'salir':
                    self.print_info("Operación cancelada")
                    input("\nPresione Enter para continuar...")
                    return
                stock = int(stock_input)
                if stock >= 0:
                    break
                self.print_error("El stock debe ser 0 o positivo")
            except ValueError:
                self.print_error("Ingrese un número entero válido")
        
        # Seleccionar categoría de la lista
        categories = self.category_service.get_all_category_names()
        
        if not categories:
            self.print_info("No hay categorías disponibles. Cree una categoría primero.")
            input("\nPresione Enter para continuar...")
            return
        
        print("\n📋 CATEGORÍAS DISPONIBLES:")
        for i, cat in enumerate(categories, 1):
            print(f"   {i}. {cat}")
        print("   0. Cancelar")
        
        while True:
            try:
                cat_option = input("\nSeleccione categoría (número): ").strip()
                if cat_option == '0' or cat_option.lower() == 'salir':
                    self.print_info("Operación cancelada")
                    input("\nPresione Enter para continuar...")
                    return
                
                cat_index = int(cat_option) - 1
                if 0 <= cat_index < len(categories):
                    categoria = categories[cat_index]
                    break
                else:
                    self.print_error(f"Seleccione un número entre 1 y {len(categories)}")
            except ValueError:
                self.print_error("Ingrese un número válido")
        
        success, message = self.product_service.add_product(
            nombre, precio, stock, categoria
        )
        
        if success:
            self.print_success(message)
        else:
            self.print_error(message)
        
        input("\nPresione Enter para continuar...")
    
    def update_product(self):
        self.clear_screen()
        self.print_header("✏️ ACTUALIZAR PRODUCTO")
        self.print_info("(Escriba 'salir' para cancelar)")
        
        self.list_products(simple=True)
        
        try:
            product_id_input = self.input_with_validation("\nID del producto a actualizar: ")
            if product_id_input == 'salir':
                self.print_info("Operación cancelada")
                input("\nPresione Enter para continuar...")
                return
            product_id = int(product_id_input)
        except ValueError:
            self.print_error("ID inválido")
            input("\nPresione Enter para continuar...")
            return
        
        product = self.product_service.get_product(product_id)
        if not product:
            self.print_error("Producto no encontrado")
            input("\nPresione Enter para continuar...")
            return
        
        print(f"\nActualizando: {product.nombre}")
        print("(Deje en blanco para mantener el valor actual, 'salir' para cancelar)")
        
        nombre = input(f"Nuevo nombre [{product.nombre}]: ").strip()
        if nombre.lower() == 'salir':
            self.print_info("Operación cancelada")
            input("\nPresione Enter para continuar...")
            return
        if not nombre:
            nombre = product.nombre
        
        try:
            precio_input = input(f"Nuevo precio [${product.precio}]: ").strip()
            if precio_input.lower() == 'salir':
                self.print_info("Operación cancelada")
                input("\nPresione Enter para continuar...")
                return
            precio = float(precio_input) if precio_input else product.precio
        except ValueError:
            precio = product.precio
        
        try:
            stock_input = input(f"Nuevo stock [{product.stock}]: ").strip()
            if stock_input.lower() == 'salir':
                self.print_info("Operación cancelada")
                input("\nPresione Enter para continuar...")
                return
            stock = int(stock_input) if stock_input else product.stock
        except ValueError:
            stock = product.stock
        
        # Seleccionar categoría de la lista
        categories = self.category_service.get_all_category_names()
        print("\n📋 CATEGORÍAS DISPONIBLES:")
        for i, cat in enumerate(categories, 1):
            print(f"   {i}. {cat}")
        print("   0. Mantener actual")
        
        current_cat_index = -1
        for i, cat in enumerate(categories):
            if cat == product.categoria:
                current_cat_index = i + 1
                break
        
        if current_cat_index > 0:
            print(f"Categoría actual: {product.categoria} (opción {current_cat_index})")
        
        while True:
            try:
                cat_option = input("\nSeleccione nueva categoría (número, 0 para mantener): ").strip()
                if cat_option == '0' or cat_option.lower() == 'salir':
                    categoria = product.categoria
                    break
                
                cat_index = int(cat_option) - 1
                if 0 <= cat_index < len(categories):
                    categoria = categories[cat_index]
                    break
                else:
                    self.print_error(f"Seleccione un número entre 0 y {len(categories)}")
            except ValueError:
                self.print_error("Ingrese un número válido")
        
        success, message = self.product_service.update_product(
            product_id, nombre, precio, stock, categoria
        )
        
        if success:
            self.print_success(message)
        else:
            self.print_error(message)
        
        input("\nPresione Enter para continuar...")
    
    def delete_product(self):
        self.clear_screen()
        self.print_header("🗑️ ELIMINAR PRODUCTO")
        self.print_info("(Escriba 'salir' para cancelar)")
        
        self.list_products(simple=True)
        
        try:
            product_id_input = self.input_with_validation("\nID del producto a eliminar: ")
            if product_id_input == 'salir':
                self.print_info("Operación cancelada")
                input("\nPresione Enter para continuar...")
                return
            product_id = int(product_id_input)
        except ValueError:
            self.print_error("ID inválido")
            input("\nPresione Enter para continuar...")
            return
        
        confirm = input(f"¿Está seguro de eliminar el producto ID {product_id}? (s/n): ")
        if confirm.lower() == 's':
            success, message = self.product_service.delete_product(product_id)
            if success:
                self.print_success(message)
            else:
                self.print_error(message)
        else:
            self.print_info("Operación cancelada")
        
        input("\nPresione Enter para continuar...")
    
    def list_products(self, simple: bool = False):
        products = self.product_service.get_all_products()
        
        if not products:
            self.print_info("No hay productos registrados")
            if not simple:
                input("\nPresione Enter para continuar...")
            return
        
        if simple:
            print("\n--- PRODUCTOS DISPONIBLES ---")
            for p in products:
                estado = "AGOTADO" if p.stock == 0 else f"Stock: {p.stock}"
                print(f"ID: {p.id} | {p.nombre} | ${p.precio:.2f} | {estado} | {p.categoria}")
        else:
            self.print_header("LISTA DE PRODUCTOS")
            print(f"{'ID':<5} {'NOMBRE':<30} {'PRECIO':<10} {'STOCK':<8} {'CATEGORÍA':<15}")
            print("-" * 70)
            for p in products:
                print(f"{p.id:<5} {p.nombre[:28]:<30} ${p.precio:<9.2f} {p.stock:<8} {p.categoria:<15}")
            print("-" * 70)
            print(f"Total: {len(products)} productos")
            input("\nPresione Enter para continuar...")
    
    def view_inventory_report(self):
        self.clear_screen()
        self.print_header("📊 INFORME DE INVENTARIO")
        
        report = self.product_service.generate_inventory_report()
        
        print(f"\n📈 ESTADÍSTICAS GENERALES:")
        print(f"   Total de productos: {report['total_products']}")
        print(f"   Total de categorías: {report['total_categories']}")
        print(f"   Productos agotados: {report['out_of_stock']}")
        print(f"   Productos con stock bajo (≤5): {report['low_stock']}")
        
        if report['out_of_stock'] > 0:
            print(f"\n⚠️ PRODUCTOS AGOTADOS:")
            for p in self.product_service.get_out_of_stock_products():
                print(f"   • {p.nombre} (Categoría: {p.categoria})")
        
        print(f"\n📋 LISTADO COMPLETO:")
        print("-" * 70)
        print(f"{'ID':<5} {'NOMBRE':<30} {'PRECIO':<10} {'STOCK':<8} {'CATEGORÍA':<15}")
        print("-" * 70)
        
        products = self.product_service.get_all_products()
        for p in products:
            print(f"{p.id:<5} {p.nombre[:28]:<30} ${p.precio:<9.2f} {p.stock:<8} {p.categoria:<15}")
        
        print("-" * 70)
        print(f"Total: {len(products)} productos")
        
        input("\nPresione Enter para continuar...")
    
    def manage_categories(self):
        while True:
            self.clear_screen()
            self.print_header("📚 GESTIÓN DE CATEGORÍAS")
            
            # Mostrar categorías existentes
            categories = self.category_service.get_all_category_names()
            
            print("\n📋 CATEGORÍAS EXISTENTES:")
            if categories:
                for i, cat in enumerate(categories, 1):
                    print(f"   {i}. {cat}")
            else:
                print("   No hay categorías registradas")
            
            print("\n1. Crear nueva categoría")
            print("2. Volver")
            
            option = input("\nSeleccione una opción: ").strip()
            
            if option == "1":
                self.create_category()
            elif option == "2":
                break
            else:
                self.print_error("Opción inválida")
                input("\nPresione Enter para continuar...")
    
    def create_category(self):
        self.clear_screen()
        self.print_header("➕ CREAR NUEVA CATEGORÍA")
        self.print_info("(Escriba 'salir' para cancelar)")
        
        nombre = self.input_with_validation("Nombre de la categoría: ")
        if nombre == 'salir':
            self.print_info("Operación cancelada")
            input("\nPresione Enter para continuar...")
            return
        
        success, message = self.category_service.create_category(nombre)
        
        if success:
            self.print_success(message)
        else:
            self.print_error(message)
        
        input("\nPresione Enter para continuar...")
    
    def client_menu(self):
        while True:
            self.clear_screen()
            nombre = self.current_user.nombres.split()[0]
            saludo = self.get_greeting(nombre)
            self.print_header(f"👤 {saludo}")
            print("\n1. Comprar")
            print("2. Ver facturas pasadas")
            print("3. Actualizar mis datos")
            print("4. Cerrar sesión")
            
            option = input("\nSeleccione una opción: ").strip()
            
            if option == "1":
                self.shopping_process()
            elif option == "2":
                self.view_invoices()
            elif option == "3":
                self.update_user_data()
            elif option == "4":
                self.current_user = None
                break
            else:
                self.print_error("Opción inválida")
                input("\nPresione Enter para continuar...")
    
    def update_user_data(self):
        self.clear_screen()
        self.print_header("✏️ ACTUALIZAR MIS DATOS")
        self.print_info("(Escriba 'salir' para cancelar)")
        
        print("(Deje en blanco para mantener el valor actual)")
        
        nombres = input(f"Nuevos nombres [{self.current_user.nombres}]: ").strip()
        if nombres.lower() == 'salir':
            self.print_info("Operación cancelada")
            input("\nPresione Enter para continuar...")
            return
        if not nombres:
            nombres = self.current_user.nombres
        
        apellidos = input(f"Nuevos apellidos [{self.current_user.apellidos}]: ").strip()
        if apellidos.lower() == 'salir':
            self.print_info("Operación cancelada")
            input("\nPresione Enter para continuar...")
            return
        if not apellidos:
            apellidos = self.current_user.apellidos
        
        print("\n¿Desea cambiar la contraseña?")
        change_password = input("(s/n): ").lower()
        
        new_password = None
        confirm_password = None
        
        if change_password == 's':
            new_password = self.input_with_validation("Nueva contraseña: ")
            if new_password == 'salir':
                self.print_info("Operación cancelada")
                input("\nPresione Enter para continuar...")
                return
            confirm_password = self.input_with_validation("Confirmar contraseña: ")
            if confirm_password == 'salir':
                self.print_info("Operación cancelada")
                input("\nPresione Enter para continuar...")
                return
        
        success, message = self.user_service.update_user_data(
            self.current_user, nombres, apellidos, new_password, confirm_password
        )
        
        if success:
            self.print_success(message)
        else:
            self.print_error(message)
        
        input("\nPresione Enter para continuar...")
    
    def shopping_process(self):
        cart = []
        
        while True:
            self.clear_screen()
            self.print_header("🛒 PROCESO DE COMPRA")
            self.print_info("(Escriba 'salir' para cancelar la compra)")
            
            categories = self.product_service.get_categories()
            
            if not categories:
                self.print_info("No hay categorías disponibles")
                input("\nPresione Enter para continuar...")
                return
            
            print("\nCATEGORÍAS DISPONIBLES:")
            for i, category in enumerate(categories, 1):
                print(f"{i}. {category}")
            print(f"{len(categories) + 1}. Ver carrito")
            print(f"{len(categories) + 2}. Finalizar compra")
            print("0. Cancelar y volver")
            
            try:
                option_input = input("\nSeleccione una opción: ").strip()
                if option_input == '0' or option_input.lower() == 'salir':
                    self.print_info("Compra cancelada")
                    input("\nPresione Enter para continuar...")
                    return
                option = int(option_input)
            except ValueError:
                self.print_error("Opción inválida")
                input("\nPresione Enter para continuar...")
                continue
            
            if 1 <= option <= len(categories):
                self.show_category_products(categories[option - 1], cart)
            elif option == len(categories) + 1:
                self.show_cart(cart)
            elif option == len(categories) + 2:
                if self.finish_purchase(cart):
                    return
            else:
                self.print_error("Opción inválida")
                input("\nPresione Enter para continuar...")
    
    def show_category_products(self, category: str, cart):
        while True:
            self.clear_screen()
            self.print_header(f"📦 CATEGORÍA: {category}")
            self.print_info("(Escriba 'salir' o '0' para volver)")
            
            products = self.product_service.get_products_by_category(category)
            
            print(f"\n{'ID':<5} {'PRODUCTO':<30} {'PRECIO':<10} {'STOCK':<8}")
            print("-" * 55)
            for p in products:
                estado = "AGOTADO" if p.stock == 0 else f"{p.stock}"
                print(f"{p.id:<5} {p.nombre[:28]:<30} ${p.precio:<9.2f} {estado:<8}")
            
            print("\n0. Volver")
            
            try:
                product_id_input = input("\nID del producto a comprar: ").strip()
                if product_id_input == '0' or product_id_input.lower() == 'salir':
                    break
                product_id = int(product_id_input)
                
                product = None
                for p in products:
                    if p.id == product_id:
                        product = p
                        break
                
                if not product:
                    self.print_error("Producto no encontrado")
                    input("\nPresione Enter para continuar...")
                    continue
                
                if product.stock == 0:
                    self.print_error("Producto agotado")
                    input("\nPresione Enter para continuar...")
                    continue
                
                quantity_input = input(f"Cantidad (máx {product.stock}): ").strip()
                if quantity_input.lower() == 'salir':
                    break
                quantity = int(quantity_input)
                
                if quantity <= 0:
                    self.print_error("La cantidad debe ser mayor que 0")
                elif quantity > product.stock:
                    self.print_error(f"Cantidad máxima disponible: {product.stock}")
                else:
                    cart.append({'product_id': product_id, 'quantity': quantity})
                    self.print_success(f"{quantity} x {product.nombre} agregado al carrito")
                
                input("\nPresione Enter para continuar...")
                
            except ValueError:
                self.print_error("Ingrese un número válido")
                input("\nPresione Enter para continuar...")
    
    def show_cart(self, cart):
        self.clear_screen()
        self.print_header("🛒 CARRITO DE COMPRAS")
        self.print_info("(Escriba 'salir' para volver)")
        
        if not cart:
            self.print_info("El carrito está vacío")
        else:
            total = 0
            print(f"\n{'PRODUCTO':<40} {'CANTIDAD':<10} {'P. UNIT':<10} {'SUBTOTAL':<10}")
            print("-" * 70)
            
            for item in cart:
                product = self.product_service.get_product(item['product_id'])
                subtotal = product.precio * item['quantity']
                total += subtotal
                print(f"{product.nombre[:38]:<40} {item['quantity']:<10} ${product.precio:<9.2f} ${subtotal:<9.2f}")
            
            print("-" * 70)
            print(f"{'TOTAL':<60} ${total:.2f}")
        
        print("\n1. Vaciar carrito")
        print("2. Seguir comprando")
        print("3. Finalizar compra")
        print("0. Volver")
        
        option = input("\nSeleccione una opción: ").strip()
        
        if option == "0" or option.lower() == 'salir':
            return
        elif option == "1":
            cart.clear()
            self.print_success("Carrito vaciado")
        elif option == "2":
            return
        elif option == "3":
            if self.finish_purchase(cart):
                return
        
        input("\nPresione Enter para continuar...")
    
    def finish_purchase(self, cart):
        if not cart:
            self.print_error("El carrito está vacío")
            input("\nPresione Enter para continuar...")
            return False
        
        self.clear_screen()
        self.print_header("📋 RESUMEN DE COMPRA")
        
        total = 0
        print(f"\n{'PRODUCTO':<40} {'CANTIDAD':<10} {'P. UNIT':<10} {'SUBTOTAL':<10}")
        print("-" * 70)
        
        for item in cart:
            product = self.product_service.get_product(item['product_id'])
            subtotal = product.precio * item['quantity']
            total += subtotal
            print(f"{product.nombre[:38]:<40} {item['quantity']:<10} ${product.precio:<9.2f} ${subtotal:<9.2f}")
        
        print("-" * 70)
        print(f"{'TOTAL':<60} ${total:.2f}")
        
        confirm = input("\n¿Confirmar compra? (s/n): ").lower()
        
        if confirm == 's':
            success, message, invoice = self.invoice_service.create_invoice(
                self.current_user.id, cart
            )
            
            if success:
                self.print_success(message)
                cart.clear()
                input("\nPresione Enter para continuar...")
                return True
            else:
                self.print_error(message)
                input("\nPresione Enter para continuar...")
                return False
        else:
            self.print_info("Compra cancelada")
            input("\nPresione Enter para continuar...")
            return False
    
    def view_invoices(self):
        self.clear_screen()
        self.print_header("📄 MIS FACTURAS")
        self.print_info("(Presione Enter para continuar)")
        
        invoices = self.invoice_service.get_user_invoices(self.current_user.id)
        
        if not invoices:
            self.print_info("No tiene facturas registradas")
        else:
            for invoice in invoices:
                print(f"\n--- FACTURA #{invoice.id} ---")
                print(f"Fecha: {invoice.fecha}")
                print(f"\n{'Producto':<40} {'Cant.':<8} {'P. Unit':<10} {'Subtotal':<10}")
                print("-" * 70)
                
                for item in invoice.items:
                    print(f"{item.producto_nombre[:38]:<40} {item.cantidad:<8} ${item.precio_unitario:<9.2f} ${item.subtotal:<9.2f}")
                
                print("-" * 70)
                print(f"{'TOTAL':<60} ${invoice.total:.2f}")
                print("=" * 70)
        
        input("\nPresione Enter para continuar...")