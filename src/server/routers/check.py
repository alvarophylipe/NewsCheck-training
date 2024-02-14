from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.server.models import PredictionItem
from src.server.request_models import PredictionItemRequest
from src.utils.tokenizer import encode
from transformers import TFBertForSequenceClassification
from src.utils.web_extraction import web_extract
from scipy.special import softmax
from numpy import argmax
from src.constants import MODEL

# Router Configs 
router = APIRouter(
    prefix="/check",
    tags=["check"],
    responses={404: {"Description": "Not found"}}
)

# Templates
templates = Jinja2Templates(directory='src/server/templates')


model = TFBertForSequenceClassification.from_pretrained(MODEL)


def predict(text):
    tokens = encode([text])
    preds = model.predict(tokens)[0]
    prediction = argmax(softmax(preds))

    return {"prediction": int(prediction)}

# HTTP Routers
@router.get('/', response_class=HTMLResponse)
async def check(request: Request):
    return templates.TemplateResponse("check.html", {'request': request})

@router.post('/process')
async def process(request: Request, prediction_item: PredictionItemRequest):

    if prediction_item.type == 'text':
        return predict(prediction_item.content)
    else:
        return predict(web_extract(prediction_item.content))

    
