from car import Car
#metodo pubico 
#print(car.manufacturer)
car = Car('SUBARU')
car.set_model('Terraneitor')
car.set_color('Red')
car.cylinder = 1.5
car.model = 'No es buena practica - Pero modificado por proterpy'

print(car.get_color())
print(car.get_model())
print("-------------------")
print(car.details())
print(car.cylinder)

print(car.accelerate_and_brake(4000,100))
#####################

mazda = Car('Mazda', 'MD-f5','black', 2.5)
print(mazda.details())
print(car)
print(repr(car))

print(mazda.accelerate(3000,100))
print(mazda.brake())

print(f'kilometros por litro: {mazda.calculate_consumption(300 ,0.6)}')
print(f'kilometros por litro: {mazda.calculate_consumption(300 ,60)}')
#########################
# mazda = Car('Mazda', 'BT-50', 'Black')
# mazda.cylinder= 1.9
# print(mazda.details())
# print(mazda.cylinder)

# mazda._other = 'Otro gato'
# print(mazda._other)

# print("============== metodo __str__ =================")
# print(car)
# print(repr(car))


################################################

# mazda = CarStation()
# mazda.manufacturer = 'Mazda'
# mazda.model = 'BT-50'
# mazda.color = 'Black'
# mazda.cylinder = 2.8

# print(f'mazda.manufacturer: ', mazda.manufacturer)
# print(f'mazda.model: ', mazda.model)
# print(f'mazda.color: ', mazda.color)
# print(f'mazda.cylinder: ', mazda.cylinder)



