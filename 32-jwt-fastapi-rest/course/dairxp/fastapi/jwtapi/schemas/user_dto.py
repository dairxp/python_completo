from pydantic import BaseModel, EmailStr


class UserDto(BaseModel):
    id:int
    email: EmailStr
    is_active: bool