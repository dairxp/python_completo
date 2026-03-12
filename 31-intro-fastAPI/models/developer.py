from typing import List, Optional

from models.experience import Experience
from models.languaje import Languajes
from models.skill import Skill
from pydantic import BaseModel


class Developer(BaseModel):
    id: int
    name: str
    country: str
    age: int
    experience: List[Experience]
    skills: List[Skill]
    languages: List[Languajes]
