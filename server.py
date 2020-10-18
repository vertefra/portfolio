from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from controllers import controller
from setup import Config
import uvicorn
import os

PORT = Config.getPort(5000)
print(PORT)

# init database

SQLALCHEMY_DATABASE_URL = "postgresql://projects"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# endinit

app = FastAPI()
app.include_router(
    controller.router,
    prefix="",
)


app.mount("/static", StaticFiles(directory="static"), name="static")

print(__name__)
if __name__ == "__main__":
    print("server running")
    uvicorn.run("server:app", host="0.0.0.0", port=int(PORT), reload=True)
