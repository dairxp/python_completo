def show_number():
    try:
        number = int(input('Ingrese un numero= '))

        print(f"El numero es : {number}")
    except Exception as e:
        print("Ocurrio un errror")


show_number()