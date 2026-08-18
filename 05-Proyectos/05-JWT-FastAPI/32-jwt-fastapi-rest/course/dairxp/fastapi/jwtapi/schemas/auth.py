from pydantic import BaseModel, EmailStr


class LoginInRequest(BaseModel):
    username: EmailStr
    password: str

class TokenDto(BaseModel):
    access_token: str
    token_type: str = 'bearer'