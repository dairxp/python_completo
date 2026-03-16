from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from course.dairxp.fastapi.jwtapi.config.settings import settings

engine = create_engine(settings.DATABASE_URL, echo=True, pool_size=10)
SessonLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base =declarative_base()

def get_db():
    db = SessonLocal()
    try:
        yield db
    finally:
        db.close()