from fastapi import Form
from pydantic import BaseModel

class PredictionItem(BaseModel):
    prediction: int