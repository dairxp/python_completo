from abc import abstractmethod,ABC
from typing import List
from course.dairxp.fastapi.jwtapi.schemas.user_dto import UserDto
from course.dairxp.fastapi.jwtapi.schemas.user_request import UserRequest


class UserService:
    @abstractmethod
    def find_all(self) -> List[UserDto]:
        pass
    @abstractmethod
    def find_by_id(self, user_id:int) -> UserDto | None:
        pass
    @abstractmethod
    def find_by_email(self, email:str) -> UserDto | None:
        pass
    @abstractmethod
    def create(self, user:UserRequest) -> UserDto:
        pass