import os

from colorama.ansi import set_title
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Settings(BaseModel):
    JWT_SECRET: str = os.getenv("JWT_SECRET", "secret-jwt")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXP_MINUTES: int = int(os.getenv("JWT_EXP_MINUTES", 60))
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")

settings = Settings()