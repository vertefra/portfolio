from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from setup import views

router = APIRouter()


@router.get("/create")
async def create_project(request: Request):
    return views.TemplateResponse("project/create.html", {"request": request})


@router.get("/{notFoundPath}")
async def notFound(request: Request):
    print(request)
    return views.TemplateResponse("layout_components/underConstruction.html", {"request": request})
