from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from setup import views

router = APIRouter()


@router.get("/")
async def index(request: Request):
    return views.TemplateResponse("index.html", {"request": request})


@router.get("/{notFoundPath}")
async def notFound(request: Request):
    print(request)
    return views.TemplateResponse("notFound.html", {"request": request})
