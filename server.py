from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from controllers import controller
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
    uvicorn.run("server:pp", port=3000, host="127.0.0.1", reload=True)
