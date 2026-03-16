from sqlalchemy.orm import Session
from fastapi.params import Depends

from course.dairxp.fastapi.jwtapi.config.db import SessionLocal
from course.dairxp.fastapi.jwtapi.respositories.sqlalchemy_user_repository import SQLAlchemyUserRepository
from course.dairxp.fastapi.jwtapi.respositories.user_repository import UserRepository
from course.dairxp.fastapi.jwtapi.services.UserServiceImpl import UserServiceImpl
from course.dairxp.fastapi.jwtapi.services.user_service import UserService


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_repository(db:Session = Depends(get_db))->UserRepository:
    return SQLAlchemyUserRepository(db)

def get_service(db: Session = Depends(get_db), repo: UserRepository = Depends(get_repository)) -> UserService:
    return UserServiceImpl(repo, db)