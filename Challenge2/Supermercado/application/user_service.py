from domain.entities import User

class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository
    
    def _generate_username(self, apellidos: str, user_id: int) -> str:
        apellidos_parts = apellidos.split()
        siglas = ''
        for part in apellidos_parts:
            if part:
                siglas += part[0].upper()
        return f"{siglas}{user_id}"
    
    def login(self, username: str, password: str):
        if not username or not password:
            return False, None, "Usuario y contraseña no pueden estar vacíos"
        
        user = self.user_repository.get_by_username(username)
        if not user:
            return False, None, "Usuario no encontrado"
        
        # Comparación directa en texto plano (sin hashlib)
        if user.password != password:
            return False, None, "Contraseña incorrecta"
        
        return True, user, "Login exitoso"
    
    def create_user(self, nombres: str, apellidos: str, password: str, role: str):
        if not nombres or not apellidos or not password or not role:
            return False, "Todos los campos son obligatorios"
        
        next_id = self.user_repository.get_next_id()
        username = self._generate_username(apellidos, next_id)
        
        new_user = User(
            id=next_id,
            nombres=nombres,
            apellidos=apellidos,
            username=username,
            password=password,  # Texto plano
            role=role,
            first_login=True
        )
        
        self.user_repository.save(new_user)
        return True, f"Usuario creado exitosamente. Username: {username}"
    
    def change_password(self, user, new_password: str, confirm_password: str):
        if not new_password or not confirm_password:
            return False, "Las contraseñas no pueden estar vacías"
        
        if new_password != confirm_password:
            return False, "Las contraseñas no coinciden"
        
        user.password = new_password  # Texto plano
        user.first_login = False
        self.user_repository.update(user)
        return True, "Contraseña cambiada exitosamente"
    
    def update_user_data(self, user, nombres: str, apellidos: str, 
                        new_password=None, confirm_password=None):
        if not nombres or not apellidos:
            return False, "Nombres y apellidos no pueden estar vacíos"
        
        user.nombres = nombres
        user.apellidos = apellidos
        
        if new_password:
            if not confirm_password:
                return False, "Debe confirmar la nueva contraseña"
            if new_password != confirm_password:
                return False, "Las contraseñas no coinciden"
            user.password = new_password  # Texto plano
        
        self.user_repository.update(user)
        return True, "Datos actualizados exitosamente"
    
    def reset_user_password(self, username: str, new_password: str):
        """Permite al administrador resetear la contraseña de un usuario"""
        if not username or not new_password:
            return False, "Usuario y contraseña son obligatorios"
        
        user = self.user_repository.get_by_username(username)
        if not user:
            return False, f"Usuario {username} no encontrado"
        
        user.password = new_password  # Texto plano
        user.first_login = True  # Forzar cambio de contraseña en próximo ingreso
        self.user_repository.update(user)
        
        return True, f"Contraseña reseteada para {username}. El usuario deberá cambiarla en su próximo ingreso."