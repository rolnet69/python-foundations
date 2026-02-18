from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class User:
    id: int
    nombres: str
    apellidos: str
    username: str
    password: str  
    role: str
    first_login: bool = True

@dataclass
class Product:
    id: int
    nombre: str
    precio: float
    stock: int
    categoria: str
    activo: bool = True

@dataclass
class Category:
    nombre: str

@dataclass
class InvoiceItem:
    producto_id: int
    producto_nombre: str
    cantidad: int
    precio_unitario: float
    
    @property
    def subtotal(self) -> float:
        return self.cantidad * self.precio_unitario

@dataclass
class Invoice:
    id: int
    usuario_id: int
    fecha: str  # Formato: "YYYY-MM-DD HH:MM:SS"
    items: list
    
    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self.items)