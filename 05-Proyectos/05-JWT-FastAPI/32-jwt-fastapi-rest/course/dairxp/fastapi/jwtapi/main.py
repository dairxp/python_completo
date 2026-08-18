from fastapi import FastAPI, Request, Depends
from fastapi.security import HTTPBearer

from course.dairxp.fastapi.jwtapi.middlewares.security_middleware import security_middleware
from course.dairxp.fastapi.jwtapi.middlewares.timing_middlewares import timing_middleware
from course.dairxp.fastapi.jwtapi.routers import users
from course.dairxp.fastapi.jwtapi.config.db import engine, Base

import course.dairxp.fastapi.jwtapi.entities.user
from course.dairxp.fastapi.jwtapi.routers.auth import router
app = FastAPI()
bearer = HTTPBearer()

Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/users", tags=["users"], dependencies=[Depends(bearer)])
app.include_router(router, prefix="/oauth", tags=["oauth"])

app.middleware('http')(timing_middleware)
app.middleware('http')(security_middleware)

@app.get("/")
def read_root():
    return {"message": "Hello World"}