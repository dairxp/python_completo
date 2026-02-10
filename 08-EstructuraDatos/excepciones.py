"""
TRY : Nuestro codigo en un caso ideal el codigo sale BIEN
"""

#try:
#except:
#finally:

"""
try:
	resultado =10/0
	print(resultado)
except ZeroDivisionError as e:
	print("El error se debe a estar dividiendo por 0")
	print(f"detalle del error{e}")

finally:
	print("Cierra ciclo de ejecución")
"""

try:
	numero=int(input("Ingrese un numero = "))
	print(numero)
except ValueError as e:
	print("Por favor ingresa un numero valido")
finally:
	print("Fin ciclo")

