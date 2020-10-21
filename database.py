from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from models import modelProject
from setup import project_config

URL = project_config.DB_URL
engine = create_engine(URL, echo=True)

if project_config.env == 'dev':
    if not database_exists(engine.url):
        create_database(engine.url)
    else:
        print("Engine connected")
        engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

db = SessionLocal()

# this actually creates the table following pydantic schema

modelProject.Base.metadata.create_all(bind=engine)
