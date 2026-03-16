from abc import abstractmethod
from typing import List

from course.dairxp.fastapi.jwtapi.schemas.user_dto import UserDto

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
    def find_by_user(self, user:str) -> UserDto | None:
        pass