from fastapi import FastAPI
from course.dairxp.fastapi.jwtapi.routers import users
from course.dairxp.fastapi.jwtapi.config.db import engine, Base

import course.dairxp.fastapi.jwtapi.entities.user
from course.dairxp.fastapi.jwtapi.routers.auth import router
app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(router, prefix="/oauth", tags=["oauth"])
@app.get("/")
def read_root():
    return {"message": "Hello World"}