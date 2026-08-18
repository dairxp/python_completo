while True:
	escritura=input("ingrese lo que deseas: \n")

	with open('documento_escritura.txt', 'a')as archivo:
		archivo.write(escritura + '\a')

	with open('documento_escritura.txt', 'r')as archivo:
		print(archivo.read())