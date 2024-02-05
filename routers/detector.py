from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
# from src.utils.tokenizer import encode
# from transformers import TFBertForSequenceClassification
# from src.modules.web_extraction import web_extract
# from scipy.special import softmax
# from numpy import argmax

# Router Configs 
router = APIRouter(
    prefix="/detector",
    tags=["detector"],
    responses={404: {"Description": "Not found"}}
)

# Templates
templates = Jinja2Templates(directory='templates')

# model = TFBertForSequenceClassification.from_pretrained('serving/saved_model')

# HTTP Routers
@router.get('/')
async def detector(request: Request):
    return templates.TemplateResponse("detector.html", {'request': request})

@router.post('/process')
async def process(request: Request, type: str = Form(...), text: str = Form(...)):
    if type == 'text':
        pass
        # tokens = encode([text])
        # preds = model.predict(tokens)[0]
        # prediction = argmax(softmax(preds))
    elif type == 'link':
        pass
        # raw = web_extract(text)
        # tokens = encode([raw])
        # preds = model.predict(tokens)[0]
        # prediction = argmax(softmax(preds))
    
    prediction = 0
    
    return {"prediction": int(prediction)}