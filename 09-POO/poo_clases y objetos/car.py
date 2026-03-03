class Car:
    def __init__(self, manufacturer : str | None = None, 
                model : str | None = None, 
                color : str | None = None, 
                cylinder : float | None =0.00,
                tank_capacity : float | None = 40.0):
        #atributo oculto __
        self.__manufacturer = manufacturer
        self.__model = model
        self.__color = color
        self.__cylinder = cylinder
        self._other = 'motor'
        self.__tank_capacity = tank_capacity

    @classmethod
    def empty(cls): 
        return cls()
    
    @classmethod
    def basic(cls, manufacturer: str, model: str):
        return cls(manufacturer, model)
    
    @classmethod
    def with_color(cls, manufacturer: str, model: str, color:str):
        return cls(manufacturer, model, color)
    
    @classmethod
    def only_color(cls, manufacturer: str, color:str):
        return cls(manufacturer, None, color)
    
    @classmethod
    def with_cylinder(cls, manufacturer: str, model: str, color:str, cylinder: float):
        return cls(manufacturer, model, color, cylinder)

    @classmethod
    def full_spec(cls, manufacturer: str, model: str, color:str, cylinder: float, tank: float):
        return cls(manufacturer, model, color,cylinder, tank)
    
    @classmethod
    def only_tank(cls, manufacturer: str, model: str, tank: float):
        return cls(manufacturer, model, None, None, tank)
    
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
    
    def accelerate(self, rpm, speed):
        return f'El auto {self.__manufacturer} acelerando a {rpm} rpm y a {speed}km/h'
    
    def brake(self):
        return f'{self.__manufacturer} {self.__model} frenando'
    

    def accelerate_and_brake(self, rpm, speed):
        accelerating = self.accelerate(rpm, speed)
        braking = self.brake()
        return f'{accelerating} \n {braking}'

    def calculate_consumption(self, km, fuel_percentage):
        if isinstance(fuel_percentage, int):
            fuel_percentage= fuel_percentage/100.00
        return km/(fuel_percentage*self.__tank_capacity)



    def __str__(self):
        return f'Car(manufacturer={self.__manufacturer}, model={self.__model}, color={self.__color}, cylinder={self.__cylinder}, tank={self.__tank_capacity})'
    def __repr__(self):
        return f'{{manufacturer: {self.__manufacturer}, model: {self.__model}, color: {self.__color}, cylinder: {self.__cylinder}, tank={self.__tank_capacity}}}'
