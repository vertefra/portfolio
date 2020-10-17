from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from controllers import controller

# router and app set up


views = Jinja2Templates(directory="views")
