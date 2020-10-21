from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from controllers import controller, projectsController
from setup import project_config
import uvicorn


PORT = project_config.PORT

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

app.mount("/static", StaticFiles(directory="static"), name="static")

print(__name__)
if __name__ == "__main__":
    print("server running")
    uvicorn.run("server:app", host="0.0.0.0", port=int(PORT), reload=True)
