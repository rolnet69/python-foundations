from domain.entities import Product, Category

class ProductService:
    def __init__(self, product_repository, category_repository):
        self.product_repository = product_repository
        self.category_repository = category_repository
    
    def add_product(self, nombre: str, precio: float, stock: int, categoria: str):
        if not nombre:
            return False, "El nombre no puede estar vacío"
        
        if precio <= 0:
            return False, "El precio debe ser mayor que 0"
        
        if stock < 0:
            return False, "El stock debe ser 0 o positivo"
        
        if not self.category_repository.exists(categoria):
            self.category_repository.save(Category(nombre=categoria))
        
        new_product = Product(
            id=0,
            nombre=nombre,
            precio=precio,
            stock=stock,
            categoria=categoria,
            activo=True
        )
        
        self.product_repository.save(new_product)
        return True, "Producto agregado exitosamente"
    
    def update_product(self, product_id: int, nombre: str, precio: float, 
                      stock: int, categoria: str):
        product = self.product_repository.get_by_id(product_id)
        if not product:
            return False, "Producto no encontrado"
        
        if not nombre:
            return False, "El nombre no puede estar vacío"
        
        if precio <= 0:
            return False, "El precio debe ser mayor que 0"
        
        if stock < 0:
            return False, "El stock debe ser 0 o positivo"
        
        if not self.category_repository.exists(categoria):
            self.category_repository.save(Category(nombre=categoria))
        
        product.nombre = nombre
        product.precio = precio
        product.stock = stock
        product.categoria = categoria
        
        self.product_repository.update(product)
        return True, "Producto actualizado exitosamente"
    
    def delete_product(self, product_id: int):
        if self.product_repository.delete(product_id):
            return True, "Producto eliminado exitosamente"
        return False, "Producto no encontrado"
    
    def get_products_by_category(self, category: str):
        return self.product_repository.get_by_category(category)
    
    def get_all_products(self):
        products = self.product_repository.get_all()
        active = []
        for p in products:
            if p.activo:
                active.append(p)
        return active
    
    def get_categories(self):
        return self.product_repository.get_categories()
    
    def get_product(self, product_id: int):
        return self.product_repository.get_by_id(product_id)
    
    def get_out_of_stock_products(self):
        products = self.get_all_products()
        out_of_stock = []
        for p in products:
            if p.stock == 0:
                out_of_stock.append(p)
        return out_of_stock
    
    def generate_inventory_report(self):
        products = self.get_all_products()
        categories = self.get_categories()
        
        out_of_stock_count = 0
        low_stock_count = 0
        for p in products:
            if p.stock == 0:
                out_of_stock_count += 1
            elif 0 < p.stock <= 5:
                low_stock_count += 1
        
        report = {
            'total_products': len(products),
            'total_categories': len(categories),
            'out_of_stock': out_of_stock_count,
            'low_stock': low_stock_count,
            'products': products,
            'categories': categories
        }
        return report