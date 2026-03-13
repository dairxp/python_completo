from fastapi import FastAPI, Response, status, HTTPException, Request, Depends
from models.developer import Developer
from typing import List, Optional
from fastapi.responses import PlainTextResponse, JSONResponse
import jwt

app = FastAPI()

developers = []

is_loggged = True

users = [{
    "username": "dairxp",
    "password": "123456"
}]

'''
@app.middleware("http")
async def check_logged(request: Request, call_next):
    #print(f'Accediendo a la ruta: {request.url}')
    if is_loggged:
        response = await call_next(request)
        return response
    return JSONResponse(content={"message": "No autizado, inicie sesión"}, status_code=401)
'''

def verify_token(request: Request):
    token = request.headers['Authorization']
    data = jwt.decode(token, "my_secret", algorithms=["HS256"])
    for user in users:
        if user['username'] == data['username']:
            return True
    return False
    
@app.post("/login")
def login(username: str, password:str):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return jwt.encode(user, "my_secret", algorithm="HS256")
    return "Datos incorrectos :("
    

@app.get("/")
def read_root():
    return {"message": "Hola mundo"}


@app.get("/developers")
def read_developers(authorized: bool = Depends(verify_token)):
    if authorized:
        return developers
    else:
        return "No autorizado"

@app.get("/developers/{id}")
def read_developer(id: int):
    for developer in developers:
        #if developer["id"] == id:
        if developer.id == id:
            return developer
    return "Developer no encontrado"


#ruta autorizado JWT
@app.get("/developers/{id}/skills")
def read_skills(id: int, authorized: bool=Depends(verify_token)):
    if authorized:
        for developer in developers:
            if developer.id  == id:
                return developer.skills
        return "Developer no encontrado"
    else: 
        return "No autoizado"

@app.get("/developers/{id}/experience")
def read_experience(id: int):
    for developer in developers:
        if developer.id == id:
            return developer.experience
    return "Developer no encontrado"


@app.get("/developers/{id}/languages")
def read_languajes(id: int):
    for developer in developers:
        if developer.id == id:
            return developer.languages
    return "Developer no encontrado"


## PoST sin clase
"""
@app.post("/developers_sin")
def create__new_developer_sin_clase(id:int, name:str, country:str, age:int, experience: List[dict], skills: List[dict], languages: List[dict]):
    developers.append({
        "id": id,
        "name": name,
        "country": country,
        "age": age,
        "experience": experience,
        "skills": skills,
        "languages": languages
    })
    return developers

"""

@app.post("/developers")
def create__new_developer(developer: Developer):
    if len(developer.name)<5:
        raise HTTPException(status_code=400, detail= "Nombre no puede tener menos de 5 caracteres")
    
    if developer.age>100:
        raise HTTPException(status_code=400, detail= "Edad Inncorrecta")
    if developer.skill>100:
        raise HTTPException(status_code=400, detail= "Requieren habilidades")
    
    developers.append(developer)
    
    return JSONResponse(status_code=201, content={"message":"Registro Correcto"})


@app.delete("/developers/{id}")
def delete_developer(id: int):
    for developer in developers:
        if developer.id == id:
            developers.remove(developer)
            return developers
    return "No encontrado"


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000)
