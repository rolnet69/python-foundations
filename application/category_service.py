
from domain.entities import Category

class CategoryService:
    def __init__(self, category_repository):
        self.category_repository = category_repository
    
    def get_all_categories(self):
        return self.category_repository.get_all()
    
    def get_all_category_names(self):
        categories = self.category_repository.get_all()
        names = []
        for cat in categories:
            names.append(cat.nombre)
        return names
    
    def create_category(self, nombre: str):
        if not nombre:
            return False, "El nombre de la categoría no puede estar vacío"
        
        if self.category_repository.exists(nombre):
            return False, f"La categoría '{nombre}' ya existe"
        
        new_category = Category(nombre=nombre)
        self.category_repository.save(new_category)
        return True, f"Categoría '{nombre}' creada exitosamente"