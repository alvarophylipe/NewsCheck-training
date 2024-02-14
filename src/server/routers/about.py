from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Router Configs
router = APIRouter(
    prefix="/about",
    tags=["about"],
    responses={404: {"Description": "Not found"}}
)

# Templates
templates = Jinja2Templates(directory='src/server/templates')

# HTTP Methods
@router.get('/')
async def about(request: Request):
    return templates.TemplateResponse("about.html", {'request': request})