class Car:
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
    
    def __str__(self):
        return f'Car(manufacturer={self.__manufacturer}, model={self.__model}, color={self.__color}, cylinder={self.__cylinder})'
    def __repr__(self):
        return f'{{manufacturer: {self.__manufacturer}, model: {self.__model}, color: {self.__color}, cylinder: {self.__cylinder}}}'
