from typing import List, Optional

from models_mongodb.experience import Experience
from models_mongodb.languaje import Languajes
from models_mongodb.skill import Skill
from pydantic import BaseModel


class Developer(BaseModel):
    _id: str
    name: str
    country: str
    age: int
    experience: List[Experience]
    skills: List[Skill]
    languages: List[Languajes]
