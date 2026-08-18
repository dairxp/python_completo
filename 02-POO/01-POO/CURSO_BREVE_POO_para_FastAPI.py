# ============================================================================
# CURSO BREVE DE POO EN PYTHON - LO FUNDAMENTAL PARA FASTAPI
# ============================================================================

# 1. CLASES Y OBJETOS - LO MÁS BÁSICO
# ============================================================================
# Una clase es un MOLDE, un objeto es una INSTANCIA de esa clase

class Persona:
    """Clase básica: molde para crear personas"""
    pass

# Crear un objeto
persona1 = Persona()  # Instancia de la clase Persona


# 2. ATRIBUTOS - DATOS DE LA CLASE
# ============================================================================

class Persona:
    # Atributos de clase (compartido por todas las instancias)
    especie = "Humano"

    def __init__(self, nombre, edad):
        # Atributos de instancia (único para cada objeto)
        self.nombre = nombre
        self.edad = edad

# Usar la clase
p1 = Persona("Juan", 25)
p2 = Persona("María", 30)

print(p1.nombre)      # Juan
print(p1.especie)     # Humano (atributo de clase)


# 3. MÉTODOS - FUNCIONES DENTRO DE LA CLASE
# ============================================================================

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método de instancia (tiene acceso a self)
    def saludar(self):
        return f"Hola, soy {self.nombre}"

    def calcular_años(self, años):
        return self.edad + años

# Usar métodos
p1 = Persona("Juan", 25)
print(p1.saludar())              # Hola, soy Juan
print(p1.calcular_años(5))       # 30


# 4. ENCAPSULACIÓN - PRIVACIDAD EN ATRIBUTOS
# ============================================================================

class Banco:
    def __init__(self, saldo):
        self.__saldo = saldo  # __ = PRIVADO (no se accede directamente)
        self._interes = 0.05  # _ = PROTEGIDO (advertencia de no tocar)
        self.titular = "Juan" # sin _ = PÚBLICO (accesible)

    # Método para acceder al saldo de forma segura
    def obtener_saldo(self):
        return self.__saldo

    # Método para modificar saldo de forma controlada
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return True
        return False

# Usar
cuenta = Banco(1000)
print(cuenta.obtener_saldo())    # 1000
cuenta.depositar(500)
print(cuenta.obtener_saldo())    # 1500
# print(cuenta.__saldo)          # ERROR: no puedo acceder directamente


# 5. PROPIEDADES (@property) - ACCESO ELEGANTE A ATRIBUTOS
# ============================================================================
# Las propiedades permiten acceder a atributos como si fueran variables,
# pero ejecutando código detrás

class Usuario:
    def __init__(self, email):
        self.__email = email

    # @property = GETTER (obtener valor)
    @property
    def email(self):
        return self.__email

    # email.setter = SETTER (establecer valor)
    @email.setter
    def email(self, nuevo_email):
        if "@" in nuevo_email:
            self.__email = nuevo_email
        else:
            raise ValueError("Email inválido")

# Usar como si fuera un atributo
user = Usuario("juan@email.com")
print(user.email)           # juan@email.com (getter)
user.email = "maria@test.com"  # setter
print(user.email)           # maria@test.com


# 6. MÉTODOS DE CLASE (@classmethod)
# ============================================================================
# Métodos que trabajan con la CLASE, no con la instancia

class Producto:
    moneda = "USD"

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # @classmethod recibe cls (la clase) en lugar de self
    @classmethod
    def cambiar_moneda(cls, nueva_moneda):
        cls.moneda = nueva_moneda

    @classmethod
    def crear_producto_gratis(cls, nombre):
        # Factory pattern: crear objetos de forma especial
        return cls(nombre, 0)

# Usar
p1 = Producto("Laptop", 1000)
p2 = Producto.crear_producto_gratis("Muestra")
Producto.cambiar_moneda("EUR")

print(p1.moneda)  # EUR (cambió para todos)


# 7. MÉTODOS ESTÁTICOS (@staticmethod)
# ============================================================================
# Métodos que NO usan self ni cls (utilidades)

class Utilidades:
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def convertir_minusculas(texto):
        return texto.lower()

# Usar sin crear instancia
print(Utilidades.sumar(5, 3))                # 8
print(Utilidades.convertir_minusculas("JUAN"))  # juan


# 8. MÉTODOS ESPECIALES (DUNDER METHODS)
# ============================================================================

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # __str__ = representación amigable (print)
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

    # __repr__ = representación técnica (debugging)
    def __repr__(self):
        return f"Producto(nombre='{self.nombre}', precio={self.precio})"

    # __len__ = len(objeto)
    def __len__(self):
        return len(self.nombre)

    # __eq__ = comparación (==)
    def __eq__(self, otro):
        return self.precio == otro.precio

# Usar
p1 = Producto("Laptop", 1000)
print(str(p1))         # Laptop - $1000
print(repr(p1))        # Producto(nombre='Laptop', precio=1000)
print(len(p1))         # 6


# 9. HERENCIA - REUTILIZAR CÓDIGO
# ============================================================================

# Clase padre (base)
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Sonido genérico"

# Clase hija (heredada)
class Perro(Animal):
    # Hereda __init__ de Animal, pero lo modifica
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llamar al __init__ de la clase padre
        self.raza = raza

    # Override: reemplazar método de la clase padre
    def hacer_sonido(self):
        return "Guau guau"

# Usar
perro = Perro("Rex", "Labrador")
print(perro.nombre)           # Rex
print(perro.hacer_sonido())   # Guau guau


# 10. POLIMORFISMO - MISMA INTERFAZ, DIFERENTES COMPORTAMIENTOS
# ============================================================================

class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Función que funciona con cualquier animal
def escuchar_sonido(animal):
    print(animal.hacer_sonido())

# Usar
perro = Perro()
gato = Gato()
escuchar_sonido(perro)  # Guau
escuchar_sonido(gato)   # Miau


# 11. COMPOSICIÓN - USAR OBJETOS DENTRO DE OBJETOS
# ============================================================================

class Direccion:
    def __init__(self, calle, ciudad):
        self.calle = calle
        self.ciudad = ciudad

class Persona:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion  # Objeto dentro de objeto

# Usar
dir = Direccion("Calle Principal 123", "Madrid")
persona = Persona("Juan", dir)
print(persona.direccion.ciudad)  # Madrid


# ============================================================================
# EJEMPLO PRÁCTICO COMPLETO
# ============================================================================

class Producto:
    """Ejemplo para entender cómo se usaría en FastAPI"""

    def __init__(self, id: int, nombre: str, precio: float):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor > 0:
            self.__precio = valor
        else:
            raise ValueError("Precio debe ser mayor a 0")

    def aplicar_descuento(self, porcentaje):
        descuento = self.__precio * (porcentaje / 100)
        return self.__precio - descuento

    def __str__(self):
        return f"Producto({self.__nombre}, ${self.__precio})"

# Usar
producto = Producto(1, "Laptop", 1500)
print(producto)                          # Producto(Laptop, $1500)
print(producto.aplicar_descuento(10))    # 1350.0
producto.precio = 1200
print(producto.precio)                   # 1200


# ============================================================================
# RESUMEN - LO ESENCIAL PARA FASTAPI
# ============================================================================
"""
✓ CLASES Y OBJETOS: Define estructura de datos
✓ __init__: Constructor, inicializa atributos
✓ self: referencia al objeto actual
✓ Atributos: datos del objeto
✓ Métodos: funciones del objeto
✓ @property: acceso elegante a atributos privados
✓ Encapsulación: __, _ para privacidad
✓ Herencia: reutilizar código
✓ Composición: objetos dentro de objetos
✓ __str__, __repr__: representación del objeto

Para FastAPI necesitas:
- Definir clases para MODELOS de datos (Pydantic)
- Usar __init__ para inicializar
- @property para validaciones
- Herencia para reutilizar modelos
- Composición para estructuras complejas
"""
