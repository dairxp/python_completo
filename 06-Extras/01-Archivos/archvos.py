"""
Lectura de estritura de archivos
Escritura
"""
#	Escritura
with open("documento.txt", "w")as archivo:
	archivo.write('manipula un documentos con python \n')
	archivo.write('manipula un documentos con python_2 \n')
	archivo.write('manipula un documentos con python_3 \t')
	archivo.write('manipula un documentos con python')

#	Lectura
with open("documento.txt", 'r')as archivo:
	print(archivo.read())
