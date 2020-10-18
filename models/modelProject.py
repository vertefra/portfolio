from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from pydantic import BaseModel

from server import Base


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    tags = Column(String)
    img_url = Column(String)
    github = Column(String)
    live = Coulm(String)


class ProjectSchema(BaseModel):
    name: str
    description: str
    tags: str = ""
    img_url: str = ""
    github: str = "github.com/vertefra"
    live: str = ""

    class Config:
        orm_mode = True
