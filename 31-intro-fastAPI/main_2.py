from typing import List, Optional

import uvicorn
from fastapi import FastAPI, Response, status
from models.developer import Developer

app = FastAPI()

developers = []


@app.get("/")
def read_root():
    return {"message": "Hola mundo"}


@app.get("/developers")
def read_developers():
    return developers


@app.get("/developers/{id}")
def read_developer(id: int):
    for developer in developers:
        #if developer["id"] == id:
        if developer.id == id:
            return developer
    return "Developer no encontrado"


@app.get("/developers/{id}/skills")
def read_skills(id: int):
    for developer in developers:
        if developer.id  == id:
            return developer.skills
    return "Developer no encontrado"


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
    developers.append(developer)
    return developers


@app.delete("/developers/{id}")
def delete_developer(id: int):
    for developer in developers:
        if developer.id == id:
            developers.remove(developer)
            return developers
    return "No encontrado"


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000)
