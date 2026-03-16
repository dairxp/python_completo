from idlelib.debugobj_r import remote_object_tree_item
from typing import List

from sqlalchemy.orm import Session

from course.dairxp.fastapi.jwtapi.entities.user import User
from course.dairxp.fastapi.jwtapi.respositories.user_repository import UserRepository
from course.dairxp.fastapi.jwtapi.schemas.user_dto import UserDto
from course.dairxp.fastapi.jwtapi.schemas.user_request import UserRequest
from course.dairxp.fastapi.jwtapi.services.user_service import UserService


class UserServiceImpl(UserService):

    def __init__(self, repo: UserRepository, db:Session):
        self._repo = repo
        self._db = db
    def find_all(self) -> List[UserDto]:
        return [UserDto.model_validate(user) for user in self._repo.find_all()]

    def find_by_id(self, user_id: int) -> UserDto | None:
        user = self._repo.find_by_id(user_id)
        if not user:
            return None
        return UserDto.model_validate(user)

    def find_by_email(self, email: str) -> UserDto | None:
        user =self._repo.find_by_email(email)
        if not user:
            return None
        return UserDto.model_validate(user)

    def create(self, user: UserRequest) -> UserDto:
        if self._repo.find_by_email(str(user.email)):
            raise ValueError('Email ya existe.')
        user_entity = User(email=user.email, password=user.password)
        try:
            saved = self._repo.create_user(user_entity)
            return UserDto.model_validate(saved)
        except Exception as e:
            self._db.rollback()
            raise
