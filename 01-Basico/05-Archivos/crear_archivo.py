#   r = READ
#   w = WRITE
#   a = APPEN
#   x = CREATE

###     read no te deja edita pero con "r+"..... no solo sera de lectura sino escritura



#nuevo_archivo =open('texto2.txt', 'x')  #Crear

#nuevo_archivo =open('texto2.txt', 'a') #append   .. añade al archivo

nuevo_archivo =open('texto2.txt', 'w') #write  .. Rescribe el archivo
nuevo_archivo.write("\nNueva line desde python")
nuevo_archivo.close()