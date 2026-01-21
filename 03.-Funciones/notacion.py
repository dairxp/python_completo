def multiplcador_palabra(texto,cantidad):
    return texto*cantidad
resultado= multiplcador_palabra("Chesper",3)
print(resultado)

def mutiplicar_notacion(texto:str, cantidad:int)->str:
    return texto*cantidad
resultado_notacion= mutiplicar_notacion("Jose", 5)
print(resultado_notacion)