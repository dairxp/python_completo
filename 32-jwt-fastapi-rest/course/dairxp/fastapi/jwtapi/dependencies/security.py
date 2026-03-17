from fastapi import HTTPException, status
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from course.dairxp.fastapi.jwtapi.config.settings import settings
from course.dairxp.fastapi.jwtapi.dependencies.di import get_repository
from course.dairxp.fastapi.jwtapi.entities.user import User
from course.dairxp.fastapi.jwtapi.respositories.user_repository import UserRepository

oautch2_scheme = OAuth2PasswordBearer(tokenUrl="/oauth/token/form")

def get_current_user(repo: UserRepository = Depends(get_repository),
                      token:str = Depends(oautch2_scheme)) -> User:
    try:
        payload = jwt.decode(token,settings.JWT_SECRET,algorithms=[settings.JWT_ALGORITHM])
        user_id = int(payload.get('sub'))
    except (JWTError, TypeError, ValueError):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token Invalido')

    user =repo.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token Invalido')

    return user