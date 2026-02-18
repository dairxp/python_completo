def calcular_precio(producto, precio, desc):
    precio_final=precio -(desc*precio)/100

    print(f"El precio del producto {producto} es :s/.{precio_final}")

calcular_precio("Pantalon",40,20)
calcular_precio("Camisa", 30,15)