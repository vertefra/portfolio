from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from models import modelProject
from setup import views
from database import db

import json


router = APIRouter()


@router.post("/")
async def create_project(request: Request, project: modelProject.ProjectSchema):
    project = modelProject.Project.create_project(db, project)
    return {"success": True, "projectCreated": project.title}


@router.get("/")
async def get_all_projects(request: Request):
    projects = modelProject.Project.get_all_projects(db)
    return views.TemplateResponse("project/index.html", context={"request": request, "projects": projects})


@router.get("/admin-index")
async def get_all_projects_admin(request: Request):
    projects = modelProject.Project.get_all_projects(db)
    return views.TemplateResponse("project/index.html",
                                  context={"request": request, "projects": projects, "admin": True})


@router.get("/{project_id}/edit")
async def edit_project(request: Request, project_id: int):
    project = modelProject.Project.get_single_project(db, project_id)
    print(project.description)
    return views.TemplateResponse("project/edit.html", context={"request": request, "project": project})


# CREATE-FORM ROUTE - GET /projects/create

@router.get("/create")
async def render_create_form(request: Request):
    return views.TemplateResponse("project/create.html", {"request": request})


# UPDATE ROUTE - PUT /projects/:id

@router.put("/{project_id}")
async def update_project(request: Request, project: modelProject.ProjectSchema, project_id: int):
    updated_id = modelProject.Project.update_project(db, project, project_id)
    return {"success": True, "projectUpdated": updated_id}


@router.get("/{notFoundPath}")
async def notFound(request: Request):
    return views.TemplateResponse("layout_components/underConstruction.html", {"request": request})
