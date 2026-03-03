# ============================================================================
# EJEMPLOS DE POO APLICADOS EN FASTAPI
# ============================================================================

# EJEMPLO 1: MODELO SIMPLE PARA UNA API
# ============================================================================

class Usuario:
    """Modelo de usuario para API"""

    def __init__(self, id: int, nombre: str, email: str, edad: int = None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.edad = edad

    def __str__(self):
        return f"Usuario({self.nombre}, {self.email})"

    def es_adulto(self):
        return self.edad >= 18 if self.edad else False

# En FastAPI usarías:
# @app.get("/usuarios/{usuario_id}")
# async def get_usuario(usuario_id: int):
#     usuario = Usuario(usuario_id, "Juan", "juan@email.com", 25)
#     return usuario


# EJEMPLO 2: ENCAPSULACIÓN Y VALIDACIÓN
# ============================================================================

class Producto:
    """Producto con validación"""

    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.__precio = precio  # Privado

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor: float):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        self.__precio = valor

    def obtener_precio_con_impuesto(self, impuesto: float = 0.21):
        return self.__precio * (1 + impuesto)

# Usar
producto = Producto("Laptop", 1000)
print(producto.obtener_precio_con_impuesto())  # 1210.0
# producto.precio = -100  # Levanta error


# EJEMPLO 3: HERENCIA - TIPOS DE USUARIOS
# ============================================================================

class UsuarioBase:
    """Clase base para usuarios"""

    def __init__(self, nombre: str, email: str):
        self.nombre = nombre
        self.email = email

    def obtener_datos(self):
        return {"nombre": self.nombre, "email": self.email}


class UsuarioAdmin(UsuarioBase):
    """Usuario administrador"""

    def __init__(self, nombre: str, email: str, nivel_permisos: int = 5):
        super().__init__(nombre, email)
        self.nivel_permisos = nivel_permisos

    def puede_eliminar(self):
        return self.nivel_permisos >= 5


class UsuarioCliente(UsuarioBase):
    """Usuario cliente"""

    def __init__(self, nombre: str, email: str, dinero_gastado: float = 0):
        super().__init__(nombre, email)
        self.dinero_gastado = dinero_gastado

    def es_cliente_vip(self):
        return self.dinero_gastado > 5000

# Usar
admin = UsuarioAdmin("Admin", "admin@email.com")
cliente = UsuarioCliente("Juan", "juan@email.com", 6000)
print(admin.puede_eliminar())      # True
print(cliente.es_cliente_vip())    # True


# EJEMPLO 4: COMPOSICIÓN - ESTRUCTURAS COMPLEJAS
# ============================================================================

class Direccion:
    """Clase para dirección"""

    def __init__(self, calle: str, ciudad: str, pais: str):
        self.calle = calle
        self.ciudad = ciudad
        self.pais = pais

    def __str__(self):
        return f"{self.calle}, {self.ciudad}, {self.pais}"


class UsuarioCompleto:
    """Usuario con dirección"""

    def __init__(self, nombre: str, email: str, direccion: Direccion):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion  # Composición

    def obtener_info(self):
        return {
            "nombre": self.nombre,
            "email": self.email,
            "direccion": str(self.direccion)
        }

# Usar
dir = Direccion("Calle Principal 123", "Madrid", "España")
usuario = UsuarioCompleto("Juan", "juan@email.com", dir)
print(usuario.obtener_info())
# {'nombre': 'Juan', 'email': 'juan@email.com', 'direccion': 'Calle Principal 123, Madrid, España'}


# EJEMPLO 5: LISTA DE OBJETOS (COMO EN UNA BD)
# ============================================================================

class Carrito:
    """Carrito de compras"""

    def __init__(self):
        self.items = []  # Lista de productos

    def agregar_producto(self, producto):
        self.items.append(producto)

    def total(self):
        return sum(item.precio for item in self.items)

    def obtener_resumen(self):
        return {
            "cantidad_items": len(self.items),
            "total": self.total(),
            "items": [item.nombre for item in self.items]
        }

# Usar
carrito = Carrito()
carrito.agregar_producto(Producto("Laptop", 1000))
carrito.agregar_producto(Producto("Mouse", 30))
print(carrito.obtener_resumen())
# {'cantidad_items': 2, 'total': 1030, 'items': ['Laptop', 'Mouse']}


# EJEMPLO 6: MÉTODOS DE CLASE - FACTORY PATTERN
# ============================================================================

class Pedido:
    """Pedido con diferentes formas de creación"""

    contador = 0  # Atributo de clase

    def __init__(self, cliente: str, total: float, estado: str = "pendiente"):
        self.id = Pedido.contador + 1
        Pedido.contador += 1
        self.cliente = cliente
        self.total = total
        self.estado = estado

    @classmethod
    def crear_pedido_vacio(cls, cliente: str):
        """Factory method: crear pedido sin total"""
        return cls(cliente, 0)

    @classmethod
    def crear_pedido_express(cls, cliente: str, total: float):
        """Crear pedido express"""
        pedido = cls(cliente, total, "en_proceso")
        return pedido

    def __str__(self):
        return f"Pedido {self.id}: {self.cliente} - ${self.total} ({self.estado})"

# Usar
p1 = Pedido("Juan", 500)
p2 = Pedido.crear_pedido_express("María", 1500)
print(p1)  # Pedido 1: Juan - $500 (pendiente)
print(p2)  # Pedido 2: María - $1500 (en_proceso)


# EJEMPLO 7: VALIDACIÓN EN __init__
# ============================================================================

class Email:
    """Validación de email"""

    def __init__(self, valor: str):
        if "@" not in valor or "." not in valor:
            raise ValueError(f"Email inválido: {valor}")
        self.valor = valor

    def __str__(self):
        return self.valor


class UsuarioValidado:
    """Usuario con validación en constructor"""

    def __init__(self, nombre: str, email_str: str):
        if not nombre or len(nombre) < 2:
            raise ValueError("Nombre inválido")

        self.nombre = nombre
        self.email = Email(email_str)  # Validar email

    def __str__(self):
        return f"{self.nombre} ({self.email})"

# Usar
try:
    usuario = UsuarioValidado("Juan", "juan@email.com")
    print(usuario)  # Juan (juan@email.com)
except ValueError as e:
    print(f"Error: {e}")

# Esto da error:
# usuario_malo = UsuarioValidado("J", "email_invalido")


# EJEMPLO 8: CONVERSIÓN A DICCIONARIO (PARA JSON)
# ============================================================================

class Libro:
    """Libro que se puede convertir a diccionario"""

    def __init__(self, titulo: str, autor: str, año: int):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def a_diccionario(self):
        """Convertir a diccionario para JSON"""
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "año": self.año
        }

    def __dict__(self):
        # O usar __dict__ que existe por defecto
        return self.__dict__

# Usar (así lo retornarías en FastAPI)
libro = Libro("1984", "George Orwell", 1949)
print(libro.a_diccionario())
# {'titulo': '1984', 'autor': 'George Orwell', 'año': 1949}


# EJEMPLO 9: HERENCIA MÚLTIPLE (POCO COMÚN, PERO ÚTIL)
# ============================================================================

class Loggeable:
    """Mixin para logging"""

    def log(self, mensaje: str):
        print(f"[LOG] {mensaje}")


class Respaldable:
    """Mixin para respaldo"""

    def hacer_respaldo(self):
        print(f"[BACKUP] Respaldo de {self.__class__.__name__}")


class BaseDatos(Loggeable, Respaldable):
    """Base de datos con logging y respaldo"""

    def __init__(self):
        self.datos = {}

    def guardar(self, clave: str, valor):
        self.log(f"Guardando {clave}")
        self.datos[clave] = valor

# Usar
bd = BaseDatos()
bd.guardar("usuario_1", "Juan")
bd.hacer_respaldo()
# [LOG] Guardando usuario_1
# [BACKUP] Respaldo de BaseDatos


# ============================================================================
# RESUMEN PARA FASTAPI
# ============================================================================
"""
En FastAPI usarás POO para:

1. MODELOS DE DATOS (Pydantic):
   - Definir estructura de datos
   - Validación automática
   - Serialización a JSON

2. SERVICIOS:
   - Lógica de negocio
   - Métodos reutilizables
   - Composición de objetos

3. REPOSITORIOS:
   - Acceso a datos (BD, archivos)
   - Métodos para CRUD

4. EXCEPCIONES:
   - Clases personalizadas para errores
   - Manejo consistente

Ejemplo en FastAPI:
```python
from fastapi import FastAPI
from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nombre: str
    email: str

class UsuarioService:
    def crear_usuario(self, datos: Usuario):
        # Lógica
        return datos

app = FastAPI()
service = UsuarioService()

@app.post("/usuarios/")
async def crear(usuario: Usuario):
    return service.crear_usuario(usuario)
```
"""
