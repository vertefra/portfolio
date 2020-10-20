from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from models import modelProject
import logging
import os


DEV_URL = "postgresql:///projects"
PROD_URL = os.environ["DATABASE_URI"]


engine = create_engine(PROD_URL)

# if not database_exists(engine.url):
#     create_database(engine.url)
# else:
#     print("Engine connected")
#     engine.connect()

engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

# this actually creates the table following pydantic schema

modelProject.Base.metadata.create_all(bind=engine)
