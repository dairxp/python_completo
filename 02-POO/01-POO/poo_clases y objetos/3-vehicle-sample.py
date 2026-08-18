from vehicle import Vehicle

car = Vehicle()
print(car)

print("===========================================")

car1 =  Vehicle('Citroen', '3')
print(car1)

car2= Vehicle('Ford', '2324','black')
print(car2)

car3 =  Vehicle('Toyota', 'Vega-12','while', 1.8)
print(car3)

car4 =  Vehicle('King Long', 'ARM-76','Red', 1.75, 50 )
print(car4)

car5 =  Vehicle('King Long', 'Impreza', tank=50.00 )
print(car5)

car6 =  Vehicle('Subaru', color='Negro')
print(car6)

car7 =  Vehicle('NISSAN', color='Gris')
print(car7)

car8 =  Vehicle(model= 'L200', cylinder=3.00)
print(car8)