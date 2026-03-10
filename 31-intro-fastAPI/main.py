from fastapi import FastAPI

app = FastAPI()

sample_message = [
    {
        'id':1,
    'text': 'Hola mundo desde fastAPI'
    }, {
        'id':2,
        'text': 'Seccion de FastAPI en proceso'
    }, {
        'id':3,
        'text': 'Este es un mensaje de prueba!'
    }
    
]

@app.get("/")
def read_root():
    return {"Hello": "World"}