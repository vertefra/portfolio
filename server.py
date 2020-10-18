from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from controllers import controller, projectsController
from setup import Config
import uvicorn
import os

PORT = Config.getPort(5000)
print(PORT)

app = FastAPI()


app.include_router(
    controller.router,
    prefix="",
)


app.include_router(
    projectsController.router,
    prefix="/projects",
    tags=["projects"]
)


# @app.post("/projects")
# async def test(request: Request):
#     return {"test": True}


app.mount("/static", StaticFiles(directory="static"), name="static")

print(__name__)
if __name__ == "__main__":
    print("server running")
    uvicorn.run("server:app", host="0.0.0.0", port=int(PORT), reload=True)
