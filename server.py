from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from controllers import controller
from setup import views
import uvicorn

app = FastAPI()
app.include_router(
    controller.router,
    prefix="",
)


app.mount("/static", StaticFiles(directory="static"), name="static")

print(__name__)
if __name__ == "__main__":
    print("server running")
    uvicorn.run("server:app", host="0.0.0.0")
