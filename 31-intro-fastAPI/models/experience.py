from pydantic import BaseModel


class Experience(BaseModel):
    title: str
    location: str
    start_date: int
