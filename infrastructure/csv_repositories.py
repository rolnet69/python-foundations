import csv
import os
from domain.entities import User, Product, Category, Invoice, InvoiceItem
from domain.interfaces import UserRepository, ProductRepository, CategoryRepository, InvoiceRepository

class CSVUserRepository(UserRepository):
    def __init__(self, file_path: str = "data/usuarios.csv"):
        self.file_path = file_path
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['id', 'nombres', 'apellidos', 'username', 'password', 'role', 'first_login'])
    
    def get_all(self):
        users = []
        with open(self.file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                users.append(User(
                    id=int(row['id']),
                    nombres=row['nombres'],
                    apellidos=row['apellidos'],
                    username=row['username'],
                    password=row['password'],
                    role=row['role'],
                    first_login=row['first_login'].lower() == 'true'
                ))
        return users
    
    def get_by_id(self, user_id: int):
        users = self.get_all()
        for u in users:
            if u.id == user_id:
                return u
        return None
    
    def get_by_username(self, username: str):
        users = self.get_all()
        for u in users:
            if u.username == username:
                return u
        return None
    
    def save(self, user):
        users = self.get_all()
        if user.id == 0:
            user.id = self.get_next_id()
        users.append(user)
        self._write_all(users)
        return user
    
    def update(self, user):
        users = self.get_all()
        for i, u in enumerate(users):
            if u.id == user.id:
                users[i] = user
                self._write_all(users)
                return True
        return False
    
    def get_next_id(self):
        users = self.get_all()
        max_id = 0
        for u in users:
            if u.id > max_id:
                max_id = u.id
        return max_id + 1
    
    def _write_all(self, users):
        with open(self.file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'nombres', 'apellidos', 'username', 'password', 'role', 'first_login'])
            for u in users:
                writer.writerow([u.id, u.nombres, u.apellidos, u.username, u.password, u.role, u.first_login])

class CSVProductRepository(ProductRepository):
    def __init__(self, file_path: str = "data/productos.csv"):
        self.file_path = file_path
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['id', 'nombre', 'precio', 'stock', 'categoria', 'activo'])
    
    def get_all(self):
        products = []
        with open(self.file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append(Product(
                    id=int(row['id']),
                    nombre=row['nombre'],
                    precio=float(row['precio']),
                    stock=int(row['stock']),
                    categoria=row['categoria'],
                    activo=row['activo'].lower() == 'true'
                ))
        return products
    
    def get_by_id(self, product_id: int):
        products = self.get_all()
        for p in products:
            if p.id == product_id:
                return p
        return None
    
    def get_by_category(self, category: str):
        products = self.get_all()
        result = []
        for p in products:
            if p.categoria == category and p.activo:
                result.append(p)
        return result
    
    def save(self, product):
        products = self.get_all()
        if product.id == 0:
            product.id = self.get_next_id()
        products.append(product)
        self._write_all(products)
        return product
    
    def update(self, product):
        products = self.get_all()
        for i, p in enumerate(products):
            if p.id == product.id:
                products[i] = product
                self._write_all(products)
                return True
        return False
    
    def delete(self, product_id: int):
        products = self.get_all()
        for p in products:
            if p.id == product_id:
                p.activo = False
                self._write_all(products)
                return True
        return False
    
    def get_next_id(self):
        products = self.get_all()
        max_id = 0
        for p in products:
            if p.id > max_id:
                max_id = p.id
        return max_id + 1
    
    def get_categories(self):
        products = self.get_all()
        categories = set()
        for p in products:
            if p.activo:
                categories.add(p.categoria)
        return sorted(list(categories))
    
    def _write_all(self, products):
        with open(self.file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'nombre', 'precio', 'stock', 'categoria', 'activo'])
            for p in products:
                writer.writerow([p.id, p.nombre, p.precio, p.stock, p.categoria, p.activo])

class CSVCategoryRepository(CategoryRepository):
    def __init__(self, file_path: str = "data/categorias.csv"):
        self.file_path = file_path
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['nombre'])
    
    def get_all(self):
        categories = []
        with open(self.file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                categories.append(Category(nombre=row['nombre']))
        return categories
    
    def save(self, category):
        categories = self.get_all()
        existe = False
        for c in categories:
            if c.nombre == category.nombre:
                existe = True
                break
        
        if not existe:
            with open(self.file_path, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([category.nombre])
        return category
    
    def exists(self, category_name: str):
        categories = self.get_all()
        for c in categories:
            if c.nombre == category_name:
                return True
        return False

class CSVInvoiceRepository(InvoiceRepository):
    def __init__(self, invoice_file: str = "data/facturas.csv", 
                 items_file: str = "data/items_facturas.csv"):
        self.invoice_file = invoice_file
        self.items_file = items_file
        self._ensure_files_exist()
    
    def _ensure_files_exist(self):
        os.makedirs(os.path.dirname(self.invoice_file), exist_ok=True)
        if not os.path.exists(self.invoice_file):
            with open(self.invoice_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['id', 'usuario_id', 'fecha'])
        
        if not os.path.exists(self.items_file):
            with open(self.items_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['factura_id', 'producto_id', 'producto_nombre', 
                               'cantidad', 'precio_unitario'])
    
    def get_by_user(self, user_id: int):
        invoices = []
        
        with open(self.invoice_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if int(row['usuario_id']) == user_id:
                    items = self._get_items(int(row['id']))
                    invoices.append(Invoice(
                        id=int(row['id']),
                        usuario_id=int(row['usuario_id']),
                        fecha=row['fecha'],
                        items=items
                    ))
        # Ordenar por fecha descendente
        return sorted(invoices, key=lambda x: x.fecha, reverse=True)
    
    def _get_items(self, invoice_id: int):
        items = []
        with open(self.items_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if int(row['factura_id']) == invoice_id:
                    items.append(InvoiceItem(
                        producto_id=int(row['producto_id']),
                        producto_nombre=row['producto_nombre'],
                        cantidad=int(row['cantidad']),
                        precio_unitario=float(row['precio_unitario'])
                    ))
        return items
    
    def save(self, invoice):
        if invoice.id == 0:
            invoice.id = self.get_next_id()
        
        with open(self.invoice_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([invoice.id, invoice.usuario_id, invoice.fecha])
        
        for item in invoice.items:
            with open(self.items_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([invoice.id, item.producto_id, item.producto_nombre,
                               item.cantidad, item.precio_unitario])
        
        return invoice
    
    def get_next_id(self):
        max_id = 0
        if os.path.exists(self.invoice_file):
            with open(self.invoice_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if int(row['id']) > max_id:
                        max_id = int(row['id'])
        return max_id + 1