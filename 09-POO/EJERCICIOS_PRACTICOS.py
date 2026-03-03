# ============================================================================
# EJERCICIOS PRÁCTICOS DE POO
# ============================================================================
# Resuelve estos ejercicios para entender mejor los conceptos

# EJERCICIO 1: CLASE BÁSICA - ESTUDIANTE
# ============================================================================
"""
Crea una clase 'Estudiante' con:
- Atributos: nombre, matricula, calificaciones (lista)
- Método __init__
- Método obtener_promedio() que calcule el promedio
- Método __str__() para representación legible
"""

class Estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        if 0 <= calificacion <= 100:
            self.calificaciones.append(calificacion)
        else:
            print("Calificación debe estar entre 0 y 100")

    def obtener_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def __str__(self):
        promedio = self.obtener_promedio()
        return f"Estudiante({self.nombre}, Promedio: {promedio:.2f})"

# Usar
est = Estudiante("Juan", "2024001")
est.agregar_calificacion(85)
est.agregar_calificacion(90)
est.agregar_calificacion(78)
print(est)  # Estudiante(Juan, Promedio: 84.33)


# EJERCICIO 2: ENCAPSULACIÓN - CUENTA BANCARIA
# ============================================================================
"""
Crea una clase 'CuentaBancaria' con:
- __saldo (privado)
- __numero_cuenta (privado)
- Métodos: depositar(), retirar(), obtener_saldo()
- Validaciones: solo números positivos
"""

class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo_inicial=0):
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depositado: ${cantidad}. Saldo actual: ${self.__saldo}")
            return True
        else:
            print("La cantidad debe ser mayor a 0")
            return False

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retirado: ${cantidad}. Saldo actual: ${self.__saldo}")
            return True
        else:
            print("Cantidad inválida o saldo insuficiente")
            return False

    def obtener_saldo(self):
        return self.__saldo

# Usar
cuenta = CuentaBancaria("123456789", 1000)
cuenta.depositar(500)      # Depositado: $500. Saldo actual: $1500
cuenta.retirar(200)        # Retirado: $200. Saldo actual: $1300
print(f"Saldo: ${cuenta.obtener_saldo()}")  # Saldo: $1300


# EJERCICIO 3: @property - TEMPERATURA
# ============================================================================
"""
Crea una clase 'Temperatura' que:
- Almacene temperatura en Celsius (privado)
- @property para obtener en Celsius
- @property para obtener en Fahrenheit
- setter para cambiar temperatura con validación
"""

class Temperatura:
    def __init__(self, celsius=0):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, valor):
        if valor >= -273.15:  # Cero absoluto
            self.__celsius = valor
        else:
            raise ValueError("Temperatura no puede ser menor al cero absoluto")

    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        self.celsius = (valor - 32) * 5/9

    def __str__(self):
        return f"{self.__celsius}°C = {self.fahrenheit:.2f}°F"

# Usar
temp = Temperatura(25)
print(temp)              # 25°C = 77.00°F
print(temp.fahrenheit)   # 77.0
temp.fahrenheit = 86     # Cambia usando Fahrenheit
print(temp.celsius)      # 30.0 (aproximado)


# EJERCICIO 4: HERENCIA - VEHÍCULOS
# ============================================================================
"""
Crea:
- Clase base 'Vehiculo' con: marca, modelo, velocidad_max
- Clase 'Auto' que herede de Vehiculo y agregue: puertas
- Clase 'Bicicleta' que herede de Vehiculo
- Método describe() en ambas
"""

class Vehiculo:
    def __init__(self, marca, modelo, velocidad_max):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_max = velocidad_max

    def describe(self):
        return f"{self.marca} {self.modelo} (Vel. max: {self.velocidad_max} km/h)"

class Auto(Vehiculo):
    def __init__(self, marca, modelo, velocidad_max, puertas):
        super().__init__(marca, modelo, velocidad_max)
        self.puertas = puertas

    def describe(self):
        base = super().describe()
        return f"{base} - {self.puertas} puertas"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, 40)
        self.tipo = "Bicicleta"

    def describe(self):
        return f"Bicicleta {self.marca} {self.modelo}"

# Usar
auto = Auto("Toyota", "Corolla", 200, 4)
bicicleta = Bicicleta("Trek", "FX 3")
print(auto.describe())        # Toyota Corolla (Vel. max: 200 km/h) - 4 puertas
print(bicicleta.describe())   # Bicicleta Trek FX 3


# EJERCICIO 5: COMPOSICIÓN - BIBLIOTECA
# ============================================================================
"""
Crea:
- Clase 'Libro' con: titulo, autor, año
- Clase 'Biblioteca' que contiene una lista de libros
- Métodos: agregar_libro(), obtener_libros(), buscar_por_autor()
"""

class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} ({self.año})"

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def obtener_libros(self):
        return [str(libro) for libro in self.libros]

    def buscar_por_autor(self, autor):
        resultados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        return [str(libro) for libro in resultados]

    def cantidad_libros(self):
        return len(self.libros)

# Usar
bib = Biblioteca("Biblioteca Municipal")
bib.agregar_libro(Libro("1984", "George Orwell", 1949))
bib.agregar_libro(Libro("Don Quijote", "Miguel de Cervantes", 1605))
bib.agregar_libro(Libro("Fundación", "Isaac Asimov", 1951))

print(f"Total de libros: {bib.cantidad_libros()}")
print(f"\nTodos los libros:")
for libro in bib.obtener_libros():
    print(f"  - {libro}")

print(f"\nLibros de Isaac Asimov:")
for libro in bib.buscar_por_autor("Isaac Asimov"):
    print(f"  - {libro}")


# EJERCICIO 6: @classmethod - CARRITO DE COMPRAS
# ============================================================================
"""
Crea una clase 'Carrito' con:
- @classmethod para crear carritos especiales
- Método para agregar items
- Método para calcular total
"""

class ItemCarrito:
    def __init__(self, nombre, precio, cantidad=1):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def subtotal(self):
        return self.precio * self.cantidad

class Carrito:
    def __init__(self, cliente=None):
        self.cliente = cliente
        self.items = []

    @classmethod
    def para_compra_rapida(cls):
        """Factory: carrito sin cliente especificado"""
        return cls("Cliente Anónimo")

    @classmethod
    def para_cliente_vip(cls, nombre_cliente):
        """Factory: carrito para cliente VIP"""
        carrito = cls(nombre_cliente)
        carrito.es_vip = True
        return carrito

    def agregar_item(self, nombre, precio, cantidad=1):
        self.items.append(ItemCarrito(nombre, precio, cantidad))

    def calcular_total(self):
        return sum(item.subtotal() for item in self.items)

    def obtener_resumen(self):
        total = self.calcular_total()
        return {
            "cliente": self.cliente,
            "cantidad_items": len(self.items),
            "total": total
        }

# Usar
carrito1 = Carrito.para_compra_rapida()
carrito1.agregar_item("Laptop", 1000, 1)
carrito1.agregar_item("Mouse", 30, 2)
print(carrito1.obtener_resumen())
# {'cliente': 'Cliente Anónimo', 'cantidad_items': 2, 'total': 1060}

carrito2 = Carrito.para_cliente_vip("Juan Pérez")
print(f"Cliente VIP: {carrito2.cliente}")


# EJERCICIO 7: POLIMORFISMO - ANIMALES
# ============================================================================
"""
Crea:
- Clase base 'Animal'
- Subclases: 'Perro', 'Gato', 'Pajaro'
- Cada uno con su propio hacer_sonido()
"""

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Sonido genérico"

    def describirse(self):
        return f"{self.nombre} hace: {self.hacer_sonido()}"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

class Pajaro(Animal):
    def hacer_sonido(self):
        return "Pío pío"

# Polimorfismo en acción
def escuchar_animales(animales):
    for animal in animales:
        print(animal.describirse())

# Usar
animales = [
    Perro("Rex"),
    Gato("Mishi"),
    Pajaro("Tweety")
]
escuchar_animales(animales)
# Rex hace: Guau guau
# Mishi hace: Miau
# Tweety hace: Pío pío


# EJERCICIO 8: DESAFÍO COMPLETO - TIENDA ONLINE
# ============================================================================
"""
Crea un sistema de tienda con:
- Clase Producto
- Clase Cliente
- Clase Pedido (composición con clientes y productos)
- Métodos para calcular totales, aplicar descuentos, etc.
"""

class Producto:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def hay_stock(self, cantidad=1):
        return self.stock >= cantidad

    def __str__(self):
        return f"{self.nombre} (${self.precio})"

class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.es_vip = False

    def __str__(self):
        tipo = " VIP" if self.es_vip else ""
        return f"Cliente{tipo}: {self.nombre}"

class Pedido:
    contador = 1

    def __init__(self, cliente):
        self.id = Pedido.contador
        Pedido.contador += 1
        self.cliente = cliente
        self.items = []  # Lista de (producto, cantidad)

    def agregar_producto(self, producto, cantidad):
        if producto.hay_stock(cantidad):
            self.items.append((producto, cantidad))
            producto.stock -= cantidad
            return True
        return False

    def calcular_subtotal(self):
        total = 0
        for producto, cantidad in self.items:
            total += producto.precio * cantidad
        return total

    def aplicar_descuento(self, porcentaje):
        if self.cliente.es_vip:
            porcentaje += 5  # VIP obtiene 5% adicional

        subtotal = self.calcular_subtotal()
        descuento = subtotal * (porcentaje / 100)
        return subtotal - descuento

    def obtener_resumen(self):
        return {
            "pedido_id": self.id,
            "cliente": str(self.cliente),
            "cantidad_productos": len(self.items),
            "total": self.aplicar_descuento(0)
        }

# Usar
cliente1 = Cliente("Juan García", "juan@email.com")
cliente1.es_vip = True

producto1 = Producto(1, "Laptop", 1000, 5)
producto2 = Producto(2, "Mouse", 30, 20)

pedido = Pedido(cliente1)
pedido.agregar_producto(producto1, 1)
pedido.agregar_producto(producto2, 2)

print(pedido.obtener_resumen())
# {'pedido_id': 1, 'cliente': 'Cliente VIP: Juan García', 'cantidad_productos': 2, 'total': 1060.0}


print("\n" + "="*60)
print("✅ TODOS LOS EJERCICIOS COMPLETADOS")
print("="*60)
