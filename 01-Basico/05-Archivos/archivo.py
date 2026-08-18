# archivo = open('text.txt', 'r');
# texto =archivo.readlines(0)[2];
# archivo.close()
# print(texto);


archivo= open('text.txt', 'r');
text= archivo.readlines();
for linea in text:
    print(linea)
archivo.close()