from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Router Configs 
router = APIRouter(
    prefix="/detector",
    tags=["detector"],
    responses={404: {"Description": "Not found"}}
)

# Templates
templates = Jinja2Templates(directory='templates')

# HTTP Routers
@router.get('/detector')
async def detector(request: Request):
    return templates.TemplateResponse("detector.html", {'request': request})