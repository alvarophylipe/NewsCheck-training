from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from server.models import PredictionItem
from server.request_models import PredictionItemRequest
from server.utils.web_extraction import web_extract
from server.utils.handlers import CustomRequestHandler


# Router Configs 
router = APIRouter(
    prefix="/check",
    tags=["check"],
    responses={404: {"Description": "Not found"}}
)

# Templates
templates = Jinja2Templates(directory='server/templates')


# HTTP Routers
@router.get('/', response_class=HTMLResponse)
async def check(request: Request):
    return templates.TemplateResponse("check.html", {'request': request})

@router.post('/process')
async def process(request: Request, prediction_item: PredictionItemRequest):

    if prediction_item.type == 'text':
        handler = CustomRequestHandler(prediction_item.content.lower())
        return handler.get_result()
    else:
        extracted_text = web_extract(prediction_item.content)
        handler = CustomRequestHandler(extracted_text)
        return handler.get_result()

    
