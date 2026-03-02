class CarStation:
    def __init__(self, manufacturer=None, model=None, color='', cylinder=0.00):
        #atributo oculto __
        self.__manufacturer = manufacturer
        self.__model = model
        self.__color = color
        self.__cylinder = cylinder
        self._other = 'motor'
    
    def set_model(self, value):
        self.__model = value
    def get_model(self):
        return self.__model
    
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, value):
        self.__model = value

    def set_color(self, value):
        self.__color = value
    def get_color(self):
        return self.__color

    @property
    def cylinder(self):
        return self.__cylinder

    @cylinder.setter
    def cylinder(self, value):
        self.__cylinder = value

    def details(self):
        detail = f'manufacturer: {self.__manufacturer} \n'
        detail += f'model: {self.__model} \n'
        detail += f'color: {self.__color} \n'
        detail += f'cylinder: {self.__cylinder} \n\n'
        return detail



#metodo pubico 
#print(car.manufacturer)
car = CarStation('subaru')
car.set_model('Terraneitor')
car.set_color('Red')
car.cylinder = 1.5
car.model = 'No es buena practica - Pero modificado por proterpy'

print(car.get_color())
print(car.get_model())
print("-------------------")
print(car.details())
print(car.cylinder)


mazda = CarStation('Mazda', 'BT-50', 'Black')
mazda.cylinder= 1.9
print(mazda.details())
print(mazda.cylinder)

mazda._other = 'Otro gato'
print(mazda._other)


# mazda = CarStation()
# mazda.manufacturer = 'Mazda'
# mazda.model = 'BT-50'
# mazda.color = 'Black'
# mazda.cylinder = 2.8

# print(f'mazda.manufacturer: ', mazda.manufacturer)
# print(f'mazda.model: ', mazda.model)
# print(f'mazda.color: ', mazda.color)
# print(f'mazda.cylinder: ', mazda.cylinder)



