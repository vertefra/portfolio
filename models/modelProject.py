from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from pydantic import BaseModel


Base = declarative_base()


class ProjectSchema(BaseModel):
    title: str
    description: str
    tags: str = ""
    img_url: str = ""
    github: str = "github.com/vertefra"
    live: str = ""


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    tags = Column(String)
    img_url = Column(String)
    github = Column(String)
    live = Column(String)

    def __repr__(self):
        return f"<title:{self.title} \n <description:{self.description}> \n"

    def get_projects(db: Session):
        return db.query(Project).all()

    def create_project(db: Session, project: ProjectSchema):
        db_project = Project(**project.dict())
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project

    def get_all_projects(db: Session):
        return db.query(Project).all()

    def get_single_project(db: Session, project: ProjectSchema, id: int):
        return db.query(Project).filter(Project.id == id)
