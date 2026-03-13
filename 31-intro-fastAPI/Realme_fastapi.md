# Resumen del proyecto FastAPI

## main_1.py
- API básica con FastAPI.
- Manejo de rutas simples, parámetros de ruta y query.
- Datos en memoria (lista de usuarios), sin base de datos.
- Ejemplo de suma, bienvenida y búsqueda de usuarios/personas.

## main_2.py
- API con autenticación JWT (token simple, no seguro para producción).
- Uso de clases y validaciones con Pydantic.
- Datos en memoria (lista de developers).
- Rutas protegidas con Depends y verificación de token.
- Ejemplo de login y manejo de errores personalizados.

## main_3.py
- API conectada a MongoDB usando motor.motor_asyncio.
- CRUD completo para developers en base de datos real.
- Conversión de ObjectId a string para serialización JSON.
- Manejo de errores y respuestas HTTP adecuadas.
- Uso de modelos Pydantic para validación de datos.

## Tests
- Se usan tests automáticos con pytest y TestClient de FastAPI.
- Los tests que hacen POST, PUT o DELETE modifican la base de datos real, a menos que se configure una base de datos de pruebas.
- Es recomendable limpiar la base de datos antes/después de los tests o usar una base de datos separada para pruebas.

## Postman
- Se puede exportar la colección de endpoints a Postman para pruebas manuales.
- Permite probar rutas, enviar datos y ver respuestas de la API fácilmente.

## Recomendaciones
- Usar una base de datos de pruebas para los tests automáticos.
- Versionar la API (ej: /v1/) para facilitar cambios futuros.
- Validar y limpiar los datos de entrada/salida para evitar errores de serialización.
