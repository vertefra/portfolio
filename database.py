from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from models import modelProject
import logging
import os


PROV_URL = "postgres://cdyfwyefnnwhmf:f24dcbf133be0b94a1aab80870e055e5d38491b9ab8ddd986b72c9c8f4ceedfd@ec2-54-158-190-214.compute-1.amazonaws.com:5432/da3qpb4pbp2f88"
DEV_URL = "postgresql:///projects"
PROD_URL = os.environ["DATABASE_URL"]


engine = create_engine(PROV_URL)

if not database_exists(engine.url):
    create_database(engine.url)
else:
    print("Engine connected")
    engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

# this actually creates the table following pydantic schema

modelProject.Base.metadata.create_all(bind=engine)
