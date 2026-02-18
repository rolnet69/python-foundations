from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def get_by_id(self, user_id: int):
        pass
    
    @abstractmethod
    def get_by_username(self, username: str):
        pass
    
    @abstractmethod
    def save(self, user):
        pass
    
    @abstractmethod
    def update(self, user):
        pass
    
    @abstractmethod
    def get_next_id(self):
        pass

class ProductRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def get_by_id(self, product_id: int):
        pass
    
    @abstractmethod
    def get_by_category(self, category: str):
        pass
    
    @abstractmethod
    def save(self, product):
        pass
    
    @abstractmethod
    def update(self, product):
        pass
    
    @abstractmethod
    def delete(self, product_id: int):
        pass
    
    @abstractmethod
    def get_next_id(self):
        pass
    
    @abstractmethod
    def get_categories(self):
        pass

class CategoryRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def save(self, category):
        pass
    
    @abstractmethod
    def exists(self, category_name: str):
        pass

class InvoiceRepository(ABC):
    @abstractmethod
    def get_by_user(self, user_id: int):
        pass
    
    @abstractmethod
    def save(self, invoice):
        pass
    
    @abstractmethod
    def get_next_id(self):
        pass