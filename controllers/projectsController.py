from fastapi import APIRouter, Request, Header
from typing import Optional
from starlette.responses import RedirectResponse
from models import modelProject
from setup import project_config
from database import db
from auth import verify_token, create_token

import json


router = APIRouter()
views = project_config.views


@router.post("/")
async def create_project(
        request: Request, project: modelProject.ProjectSchema):
    project_created = modelProject.Project.create_project(db, project)
    if project_created is not False:
        return {"success": True, "projectCreated": project_created.title}
    else:
        return {"success": False, "message": "failed creating new project"}


@router.get("/")
async def get_all_projects(request: Request):
    projects = modelProject.Project.get_all_projects(db)
    return views.TemplateResponse(
        "project/index.html", context={
            "request": request, "projects": projects})


@router.get("/admin-index")
async def get_all_projects_admin(request: Request, authorization: str = Header(None)):

    if authorization == None:
        print("NO AUTH")
        return views.TemplateResponse("router/login.html", context={"request": request})

    try:
        if verify_token(authorization):

            print("AUTHORIZED")

            projects = modelProject.Project.get_all_projects(db)
            return views.TemplateResponse(
                "project/index.html", status_code=200, context={"request": request,
                                                                "projects": projects,
                                                                "admin": True})

    except Exception as err:

        print("NOT VALID TOKEN")

        return {"success": False, "error": err}

        # return views.TemplateResponse(
        #     "project/index.html",
        #     context={"request": request, "projects": projects, "admin": True})

# DELETE - delete the project - GET /projects/{id}/delete


@router.get("/{project_id}/delete")
async def delete_project(request: Request, project_id: int):
    if modelProject.Project.delete_project(db, project_id):
        projects = modelProject.Project.get_all_projects(db)
        return views.TemplateResponse(
            "project/index.html",
            context={"request": request, 'projects': projects})
    else:
        return views.TemplateResponse(
            "project/index.html",
            context={"request": request, 'flashMessage': "an error occurred"})

# EDIT - get the edit form - GET /projects/{id}/edit


@router.get("/{project_id}/edit")
async def edit_project(request: Request, project_id: int):
    project = modelProject.Project.get_single_project(db, project_id)
    return views.TemplateResponse(
        "project/edit.html", context={"request": request, "project": project})


# CREATE-FORM ROUTE - GET /projects/create

@router.get("/create")
async def render_create_form(request: Request):
    return views.TemplateResponse("project/create.html", {"request": request})


# UPDATE ROUTE - PUT /projects/:id

@router.put("/{project_id}")
async def update_project(
        request: Request,
        project: modelProject.ProjectSchema,
        project_id: int):

    updated_id = modelProject.Project.update_project(db, project, project_id)
    return {"success": True, "projectUpdated": updated_id}


@router.get("/{notFoundPath}")
async def notFound(request: Request):
    return views.TemplateResponse(
        "layout_components/underConstruction.html", {"request": request})
