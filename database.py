from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from models import modelProject
import logging

URL = "postgresql:///projects"

engine = create_engine(URL, echo=True)

if not database_exists(engine.url):
    create_database(engine.url)
else:
    print("Engine connected")
    engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

# modelProject.Base.metadata.create_all(bind=engine)
