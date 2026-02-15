class Perro:   
    def __init__(self, nombre, raza):

        print(f"Creando perro {nombre}, {raza}")
        self.nombre=nombre
        self.raza=raza

    #metodo ladra
    def ladra(self):
        print("Guau")
    #etodo camina
    def caminar(self, pasos):
        print(f"Camina {pasos} pasos")


#Atributos de  insidencia
mi_perro=Perro("toby","Big")
print("alias: ", mi_perro.nombre)
print("raza: ", mi_perro.raza)

mi_perro.ladra()
mi_perro.caminar(10)