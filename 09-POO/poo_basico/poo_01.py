class Perro:   
    def __init__(self, nombre, raza):

        print(f"Creando perro {nombre}, {raza}")
        self.nombre=nombre
        self.raza=raza

#Crear mi objeto
mi_perro=Perro("toby","Big")
print("alias: ", mi_perro.nombre)
print("raza: ", mi_perro.raza)