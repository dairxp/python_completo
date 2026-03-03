# models.py
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Product:
    id: int | None
    name: str
    price: float
    created_at: datetime