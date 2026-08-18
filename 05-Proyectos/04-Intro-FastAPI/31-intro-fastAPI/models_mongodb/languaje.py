from pydantic import BaseModel


class Languajes(BaseModel):
    name: str
    level: str
