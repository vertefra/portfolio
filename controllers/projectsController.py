from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from models import modelProject
from setup import views
from database import db


router = APIRouter()


@router.post("/")
async def create_project(project: modelProject.ProjectSchema):
    project = modelProject.Project.create_project(db, project)
    print(project)
    # return RedirectResponse("/")
    return {"success": True, "createdProject": project}


@ router.get("/create")
async def render_create_form(request: Request):
    return views.TemplateResponse("project/create.html", {"request": request})


@ router.get("/{notFoundPath}")
async def notFound(request: Request):
    return views.TemplateResponse("layout_components/underConstruction.html", {"request": request})
