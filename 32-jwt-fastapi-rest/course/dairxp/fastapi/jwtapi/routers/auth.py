from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends

from course.dairxp.fastapi.jwtapi.dependencies.di import get_service, get_repository
from course.dairxp.fastapi.jwtapi.respositories.user_repository import UserRepository
from course.dairxp.fastapi.jwtapi.schemas.auth import TokenDto, LoginInRequest
from course.dairxp.fastapi.jwtapi.security.jwt import create_access_token
from course.dairxp.fastapi.jwtapi.security.password import verify_password
from course.dairxp.fastapi.jwtapi.services.user_service import UserService

router = APIRouter()
@router.post('/token', response_model=TokenDto)
def login(data:LoginInRequest, repository:UserRepository = Depends(get_repository)):
    user = repository.find_by_email(str(data.username))
    if not user or not verify_password(data.password, str(user.password)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "Incorrect email or password")
    token =create_access_token(subject=str(user.id))
    return TokenDto(access_token=token)