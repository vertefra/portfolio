from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from setup import project_config
from auth import create_token

router = APIRouter()

views = project_config.views
PSW = project_config.PSW


@router.get("/")
async def index(request: Request):
    return views.TemplateResponse("router/index.html", {"request": request})


@router.get("/login")
async def login(request: Request):
    return views.TemplateResponse("router/login.html", {"request": request})


@router.get("/about")
async def about(request: Request):
    return views.TemplateResponse("router/about.html", {"request": request})


# check the password and send the token

@router.post("/login/")
async def login(body: dict):
    if(body["psw"] == PSW):

        # this is part of the payload for the encrypted signature

        token = create_token({'admin': 'verte'})

        return {"success": True, "token": token}
    else:
        return {"success": False, "message": "password is not correct"}


@router.get("/{notFoundPath}")
async def notFound(request: Request):
    return views.TemplateResponse("layout_components/underConstruction.html", {"request": request})
