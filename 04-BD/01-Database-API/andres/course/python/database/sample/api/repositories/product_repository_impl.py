from typing import List, Optional

import mysql.connector

from andres.course.python.database.sample.api.database_connection import DatabaseConnection
from andres.course.python.database.sample.api.models.product import Product
from andres.course.python.database.sample.api.repositories.product_repository import Repository


class ProductRepositoryImpl(Repository):

    def find_all(self) -> List[Product]:
        db = DatabaseConnection()  # Siempre devuelve la misma instancia
        connection = db.get_connection()
        products: List[Product] = []
        try:
            # Conexión a la base de datos (se cierra automáticamente al salir del bloque with)
            # with db.get_connection() as connection:

            # Crear cursor (también se cierra automáticamente)
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, price, created_at FROM products")
                for product_id, name, price, created_at in cursor.fetchall():
                    products.append(Product(product_id, name, price, created_at))

        except mysql.connector.Error as e:
            print("Error al conectar o consultar la base de datos:", e)
            raise

        return products

    def find_by_id(self, product_id: int) -> Optional[Product]:
        connection = DatabaseConnection().get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, name, price, created_at FROM products WHERE id = %s",
                    (product_id,)
                )
                row = cursor.fetchone()

                if row:
                    return Product(
                        id=row[0],
                        name=row[1],
                        price=row[2],
                        created_at=row[3]
                    )
        except mysql.connector.Error as e:
            print("Error al conectar o consultar la base de datos:", e)

        return None

    def save(self, product: Product) -> Product:
        connection = DatabaseConnection().get_connection()

        try:
            if product.id is not None and product.id > 0:
                # UPDATE
                sql = """
                    UPDATE products
                    SET name = %s, price = %s
                    WHERE id = %s
                """
                values = (product.name, product.price, product.id)
            else:
                # INSERT
                sql = """
                    INSERT INTO products (name, price, created_at)
                    VALUES (%s, %s, %s)
                """
                values = (product.name, product.price, product.created_at)

            with connection.cursor() as cursor:
                cursor.execute(sql, values)
                connection.commit()

                # Si es un insert, asignar el id generado al objeto
                if cursor.lastrowid:
                    product.id = cursor.lastrowid
        except mysql.connector.Error as e:
            print("Error al conectar o consultar la base de datos:", e)

        return product

    def remove(self, product_id: int) -> bool:
        connection = DatabaseConnection().get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
                connection.commit()
                return cursor.rowcount > 0  # True si borró algún registro
        except mysql.connector.Error as e:
            print("Error al conectar o consultar la base de datos:", e)

        return False

