import time
from domain.entities import Invoice, InvoiceItem

class InvoiceService:
    def __init__(self, invoice_repository, product_repository):
        self.invoice_repository = invoice_repository
        self.product_repository = product_repository
    
    def create_invoice(self, user_id: int, cart_items):
        if not cart_items:
            return False, "El carrito está vacío", None
        
        invoice_items = []
        for item in cart_items:
            product = self.product_repository.get_by_id(item['product_id'])
            if not product or not product.activo:
                return False, f"Producto ID {item['product_id']} no encontrado", None
            
            if product.stock < item['quantity']:
                return False, f"Stock insuficiente para {product.nombre}", None
            
            invoice_items.append(InvoiceItem(
                producto_id=product.id,
                producto_nombre=product.nombre,
                cantidad=item['quantity'],
                precio_unitario=product.precio
            ))
            
            product.stock -= item['quantity']
            self.product_repository.update(product)
        
        # Fecha en formato string: "YYYY-MM-DD HH:MM:SS"
        fecha_actual = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        
        invoice = Invoice(
            id=0,
            usuario_id=user_id,
            fecha=fecha_actual,
            items=invoice_items
        )
        
        saved_invoice = self.invoice_repository.save(invoice)
        return True, "Compra realizada exitosamente", saved_invoice
    
    def get_user_invoices(self, user_id: int):
        return self.invoice_repository.get_by_user(user_id)