# 🎯 GUÍA RÁPIDA DE POO EN PYTHON

## 1️⃣ LO BÁSICO - CLASES Y OBJETOS

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo
        self.edad = edad

    def saludar(self):  # Método
        return f"Hola, soy {self.nombre}"

# Crear un objeto
persona = Persona("Juan", 25)
print(persona.saludar())  # Hola, soy Juan
```

## 2️⃣ ATRIBUTOS: PÚBLICO, PROTEGIDO, PRIVADO

| Tipo | Sintaxis | Acceso | Uso |
|------|----------|--------|-----|
| Público | `self.nombre` | Directo desde cualquier lado | Datos públicos |
| Protegido | `self._nombre` | Acceso, pero se advierte no tocar | Uso interno |
| Privado | `self.__nombre` | Solo dentro de la clase | Datos sensibles |

```python
class Banco:
    def __init__(self):
        self.titular = "Juan"        # Público
        self._interes = 0.05         # Protegido
        self.__saldo = 1000          # Privado

    def obtener_saldo(self):
        return self.__saldo          # Acceso a privado desde dentro

cuenta = Banco()
print(cuenta.titular)       # ✓ Funciona
print(cuenta._interes)      # ✓ Funciona (pero no deberías)
print(cuenta.__saldo)       # ✗ ERROR
print(cuenta.obtener_saldo())  # ✓ Funciona
```

## 3️⃣ @property - ACCESO ELEGANTE

```python
class Usuario:
    def __init__(self, email):
        self.__email = email

    @property  # GETTER - obtener valor
    def email(self):
        return self.__email

    @email.setter  # SETTER - establecer valor
    def email(self, nuevo_email):
        if "@" in nuevo_email:
            self.__email = nuevo_email
        else:
            raise ValueError("Email inválido")

user = Usuario("juan@email.com")
print(user.email)           # juan@email.com (getter)
user.email = "maria@test.com"  # setter (ejecuta validación)
```

## 4️⃣ @classmethod - MÉTODOS DE CLASE

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @classmethod  # Trabaja con la CLASE, no con instancias
    def crear_gratis(cls, nombre):
        return cls(nombre, 0)  # Factory pattern

producto = Producto.crear_gratis("Muestra")
print(producto.precio)  # 0
```

## 5️⃣ @staticmethod - FUNCIONES DENTRO DE CLASE

```python
class Utilidades:
    @staticmethod  # No usa self, no usa cls
    def sumar(a, b):
        return a + b

print(Utilidades.sumar(5, 3))  # 8
# No necesitas crear una instancia
```

## 6️⃣ MÉTODOS ESPECIALES

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):          # print(objeto)
        return f"{self.nombre} - ${self.precio}"

    def __repr__(self):         # repr(objeto) - debugging
        return f"Producto('{self.nombre}', {self.precio})"

    def __eq__(self, otro):     # objeto1 == objeto2
        return self.precio == otro.precio

    def __lt__(self, otro):     # objeto1 < objeto2
        return self.precio < otro.precio

    def __len__(self):          # len(objeto)
        return len(self.nombre)

p1 = Producto("Laptop", 1000)
print(str(p1))      # Laptop - $1000
print(repr(p1))     # Producto('Laptop', 1000)
print(len(p1))      # 6
```

## 7️⃣ HERENCIA - REUTILIZAR CÓDIGO

```python
# Clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Sonido genérico"

# Clase hija
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llamar a clase padre
        self.raza = raza

    def hacer_sonido(self):  # Override (reemplazar)
        return "Guau guau"

perro = Perro("Rex", "Labrador")
print(perro.nombre)          # Rex (heredado)
print(perro.hacer_sonido())  # Guau guau (override)
```

## 8️⃣ POLIMORFISMO

```python
class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Una función funciona con cualquier animal
def escuchar(animal):
    print(animal.hacer_sonido())

escuchar(Perro())  # Guau
escuchar(Gato())   # Miau
```

## 9️⃣ COMPOSICIÓN - OBJETOS DENTRO DE OBJETOS

```python
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Auto:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor  # Composición

auto = Auto("Toyota", Motor(200))
print(auto.motor.potencia)  # 200
```

## 🔟 RESUMEN PARA FASTAPI

```python
# EJEMPLO COMPLETO
class Usuario:
    def __init__(self, id: int, nombre: str, email: str):
        self.id = id
        self.nombre = nombre
        self.__email = email  # Privado

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        if "@" in valor:
            self.__email = valor

    def a_diccionario(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.__email
        }

# EN FASTAPI:
# @app.post("/usuarios/")
# async def crear_usuario(usuario: Usuario):
#     return usuario.a_diccionario()
```

## 📋 CHECKLIST IMPORTANTE

- ✅ `__init__`: Siempre inicializa atributos
- ✅ `self`: Primera parámetro de métodos de instancia
- ✅ `cls`: Primera parámetro de @classmethod
- ✅ Encapsulación: Usa `__` para datos privados
- ✅ @property: Para acceso elegante con validación
- ✅ Herencia: Para reutilizar código (Animal > Perro)
- ✅ Composición: Para estructuras complejas
- ✅ `__str__`: Para representación legible
- ✅ Polimorfismo: Diferentes clases, misma interfaz

## ❌ ERRORES COMUNES

```python
# ❌ MAL: Olvidar self
class Persona:
    def saludar():  # Falta self
        print("Hola")

# ✅ BIEN:
class Persona:
    def saludar(self):
        print("Hola")

# ❌ MAL: No usar super() en herencia
class Perro(Animal):
    def __init__(self, nombre, raza):
        self.nombre = nombre  # Repite código
        self.raza = raza

# ✅ BIEN:
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Reutiliza
        self.raza = raza

# ❌ MAL: Mezclar acceso privado
clase.instancia.__atributo  # No funciona

# ✅ BIEN:
def obtener_atributo(self):
    return self.__atributo
```

## 🚀 PRÓXIMO PASO: FASTAPI

Ya sabes POO, ahora necesitas:
1. **Pydantic**: Define modelos de datos con validación
2. **FastAPI**: Usa esos modelos en rutas
3. **Bases de datos**: ORM como SQLAlchemy (clases para tablas)
