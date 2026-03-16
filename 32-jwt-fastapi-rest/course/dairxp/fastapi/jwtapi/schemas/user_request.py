from pydantic import BaseModel, EmailStr,Field

class UserRequest(BaseModel):
    email: EmailStr
    password: str =Field(..., min_length=4, max_length=32)