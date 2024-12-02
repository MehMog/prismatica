from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    image_files = os.listdir("static/images")
    image_files = [f for f in image_files if f.endswith(".avif")]
    return templates.TemplateResponse("index.html", {"request": request, "images": image_files})

@app.get("/view/{image_name}", response_class=HTMLResponse)
async def view_image(request: Request, image_name: str):
    return templates.TemplateResponse("view_image.html", {"request": request, "image_name": image_name})