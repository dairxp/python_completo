from car import Car

car = Car().empty()
print(car)

print("===========================================")

car1 =  Car.basic('Citroen', '3')
print(car1)

car2= Car.with_color('Ford', '2324','black')
print(car2)

car3 =  Car.with_cylinder('Toyota', 'Vega-12','while', 1.8)
print(car3)

car4 =  Car.full_spec('King Long', 'ARM-76','Red', 1.75, 50 )
print(car4)

car5 =  Car.only_tank('King Long', 'Impreza', tank=50.00 )
print(car5)

car6 =  Car.only_color('Subaru', color= 'Negro')
print(car6)