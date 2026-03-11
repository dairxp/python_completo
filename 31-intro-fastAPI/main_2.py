from fastapi import FastAPI, status, Response
import uvicorn
from typing import List,Optional

app = FastAPI()

developers = []

@app.get("/")
def read_root():
    return {"message": "Hola mundo"}

@app.get("/developers")
def read_developers():
    return developers

@app.get("/developers/{id}")
def read_developers(id:int):
    for developer in developers:
        if developer['id'] == id:
            return developer
    return "Developer no encontrado"

@app.get("/developers/{id}/skills")
def read_developers(id:int):
    for developer in developers:
        if developer['id'] == id:
            return developer['skills']
    return "Developer no encontrado"

@app.get("/developers/{id}/experience")
def read_developers(id:int):
    for developer in developers:
        if developer['id'] == id:
            return developer['experience']
    return "Developer no encontrado"

@app.get("/developers/{id}/languages")
def read_developers(id:int):
    for developer in developers:
        if developer['id'] == id:
            return developer['languages']
    return "Developer no encontrado"

## PoST

@app.post("/developers")
def create_developer(id:int, name:str, country:str, age:int, experience: List[dict], skills: List[dict], languages: List[dict]):
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


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=5000)

