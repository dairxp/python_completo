from http import client
from fastapi import FastAPI, Depends
from models_mongodb.developer import Developer
from fastapi.responses import JSONResponse
import motor.motor_asyncio
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

app = FastAPI()
developers = []


    
async def connection():
    client= motor.motor_asyncio.AsyncIOMotorClient('mongodb://127.0.0.1:27017')
    db =client['db_fastapi_intro']
    return db

@app.get("/developers")
async def get_developers():
    try:
        db = await connection()
        developers =await db.developers.find().to_list(1000)
        for developer in developers:
            developer['id'] = str(developer['_id'])
            del developer['_id']
        return JSONResponse(status_code=200, content={'data':developers})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message':"Ocurrio un error"})

@app.get("/developers/{id}")
async def read_developer(id: str):
    try:
        db = await connection()
        developer = await db.developers.find_one({"_id": ObjectId(id)})
        if developer:
            developer['id'] = str(developer['_id'])
            del developer['_id']
            return JSONResponse(status_code=200, content={'data': developer})
        else:
            return JSONResponse(status_code=404, content={'message': "No encontrado"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message':"Ocurrio un error"})


@app.get("/developers/{id}/skills")
async def read_skills(id: str):
    try:
        db = await connection()
        developer = await db.developers.find_one({"_id": ObjectId(id)})
        if developer:
            developer['id'] = str(developer['_id'])
            del developer['_id']
            return JSONResponse(status_code=200, content={'data': developer['skills']})
        else:
            return JSONResponse(status_code=404, content={'message': "No encontrado"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message':"Ocurrio un error"})


@app.get("/developers/{id}/experience")
async def read_experience(id: str):
    try:
        db = await connection()
        developer = await db.developers.find_one({"_id": ObjectId(id)})
        if developer:
            developer['id'] = str(developer['_id'])
            del developer['_id']
            return JSONResponse(status_code=200, content={'data': developer['experience']})
        else:
            return JSONResponse(status_code=404, content={'message': "No encontrado"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message':"Ocurrio un error"})


@app.get("/developers/{id}/languages")
async def read_languajes(id: str):
    try:
        db = await connection()
        developer = await db.developers.find_one({"_id": ObjectId(id)})
        if developer:
            developer['id'] = str(developer['_id'])
            del developer['_id']
            return JSONResponse(status_code=200, content={'data': developer['languages']})
        else:
            return JSONResponse(status_code=404, content={'message': "No encontrado"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message':"Ocurrio un error"})


@app.post("/developers")
async def create_new_developer(developer: Developer):
    try:
        db =await connection()
        await db.developers.insert_one(jsonable_encoder(developer))
        return JSONResponse(status_code=201, content={'message':"Desarrollador registrado"})
    except:
        return JSONResponse(status_code=500, content={'message':"Ocurrio un error"})

@app.put('/developers/{id}')
async def udpate_developer(data: Developer, id: str):
    try:
        db= await connection()
        developer= await db.developers.find_one({"_id":ObjectId(id)})
        if  developer:
            await db.developers.update_one({'_id': ObjectId(id)},{'$set': jsonable_encoder(data)})            
            return JSONResponse(status_code=201, content={'message': 'Desarrollador modificado'})
        else:
            return JSONResponse(status_code=400, content={'message': "No encontrado"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message':"Ocurrio un error"})

@app.delete("/developers/{id}")
async def delete_developer(id: str):
    try:
        db= await connection()
        developer= await db.developers.find_one({"_id":ObjectId(id)})
        if  developer:
            await db.developers.delete_one({'_id': ObjectId(id)})            
            return JSONResponse(status_code=200, content={'message': 'Desarrollador eliminado'})
        else:
            return JSONResponse(status_code=400, content={'message': "No encontrado"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message':"Ocurrio un error"})
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000)
