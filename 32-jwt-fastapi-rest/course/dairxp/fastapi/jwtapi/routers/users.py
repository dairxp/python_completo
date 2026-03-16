from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from starlette import status

from course.dairxp.fastapi.jwtapi.dependencies.di import get_service
from course.dairxp.fastapi.jwtapi.schemas.user_dto import UserDto
from course.dairxp.fastapi.jwtapi.schemas.user_request import UserRequest
from course.dairxp.fastapi.jwtapi.services.user_service import UserService

router = APIRouter()
@router.get('/', response_model=List[UserDto])
def list_users(service: UserService = Depends(get_service)):
    return service.find_all()

@router.get('/{user_id}', response_model=UserDto)
def get_user(user_id: int ,service:UserService = Depends(get_service)):
    user = service.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User no existe")
    return user

@router.post('/', response_model=UserDto, status_code=status.HTTP_201_CREATED)
def create_user(user: UserRequest, service: UserService = Depends(get_service)):
    try:
        return service.create(user)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))