from fastapi import FastAPI
from course.dairxp.fastapi.jwtapi.routers import users
from course.dairxp.fastapi.jwtapi.config.db import engine, Base

import course.dairxp.fastapi.jwtapi.entities.user

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Hello World"}