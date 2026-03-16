from fastapi import FastAPI
from course.dairxp.fastapi.jwtapi.config.db import engine, Base
import course.dairxp.fastapi.jwtapi.entities.user

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello World"}