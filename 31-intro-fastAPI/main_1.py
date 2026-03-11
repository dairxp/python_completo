from fastapi import FastAPI, status, Response
import uvicorn
from typing import Optional

app = FastAPI()

users = [
    {
        "id": 1,
        "name": "Juan",
        "apellido": "Perez",
        "email": "Juanito@gmail.com",
        "edad" : 10
    },
    {
        "id": 2,
        "name": "Jose",
        "apellido": "Jose",
        "email": "josemaria@gmail.com",
        "edad" : 20
    },
    {
        "id": 3,
        "name": "Pepe",
        "apellido": "fuente",
        "email": "fuenteariante@gmail.com",
        "edad" : 30
    }
]

@app.get("/")
def read_root():
    return {"message": "Hola mundo"}

@app.get("/users")
def read_users():
    return users

@app.get("/user/{id}/edad/{edad}")
def read_user(id, edad):
    print(edad)
    for user in users:
        if user["id"] == int(id) and user['edad']==int(edad):
            return user
    return "Usuario no encontrado"

#Parametros QUery
#           http://127.0.0.1:8000/person/2?edad=20&name=Jose
@app.get("/person/{id}")
def read_person(id, edad, name:Optional[str]=None):

    if not name:
        print("no se envio parametro nombre")
    else:
        print("se envio parametro nombre")

    for person in users:
        if person['id'] == int(id) and person['edad']==int(edad):
            return person
    return "Persona no encontrada"

@app.get('/welcome/{nombre}/{apellido}', status_code=status.HTTP_200_OK)
def welcome(nombre: str, apellido: str):

    return f"Bienvenido {nombre} {apellido.upper()}"

@app.get('/suma/{numero1}/{numero2}')
def sumar(numero1:int, numero2:int, response: Response):
    if numero1+numero2 > 0:
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST

    #return numero1+numero2

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=5000)

