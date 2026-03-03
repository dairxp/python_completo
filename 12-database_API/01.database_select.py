import mysql.connector

def list_products():
    try:
        # La conexión se cierra automáticamente al salir del bloque
        with mysql.connector.connect(
            host="localhost",
            user="root",
            password="951024451",
            database="py_database_api"
        ) as connection:

            print("Conexión exitosa")

            # El cursor también se cierra automáticamente
            with connection.cursor(dictionary=True) as cursor:

                query = "SELECT id, name, price, created_at FROM products"
                cursor.execute(query)
                products = cursor.fetchall()

                print("\nLista de productos:")
                for product in products:
                    print(
                        f"ID: {product['id']}, "
                        f"Nombre: {product['name']}, "
                        f"Precio: {product['price']}, "
                        f"Fecha: {product['created_at']}"
                    )

    except mysql.connector.Error as e:
        print("Error en la base de datos:", e)


if __name__ == "__main__":
    list_products()