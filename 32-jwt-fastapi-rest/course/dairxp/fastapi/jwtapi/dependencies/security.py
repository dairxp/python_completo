from urllib.request import Request

from fastapi import HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from course.dairxp.fastapi.jwtapi.entities.user import User

oautch2_scheme = OAuth2PasswordBearer(tokenUrl="/oauth/token/form")

def get_current_user(request: Request) -> User:
    user: User =request.state.user
    return user