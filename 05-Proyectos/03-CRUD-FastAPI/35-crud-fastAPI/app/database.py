from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from fastapi import Depends

#from sqlalchemy import create_engine
#engine = create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase")

DATABASE_URL = 'postgresql+psycopg://postgres:951024451@localhost:5432/ecommerce_db'

engine =create_engine(DATABASE_URL)
SeccionmLocal = sessionmaker(autocommit=False, autoflush =False, bind=engine)

Base=declarative_base()

def get_db():
    db=SeccionmLocal()
    try:
        yield db
    finally:
        db.close()

