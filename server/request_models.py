from fastapi import Form
from pydantic import BaseModel, Field

class PredictionItemRequest(BaseModel):
    type: str = Field(..., description="link or text", max_length=4)
    content: str = Field(..., description="link or text > 30 words")

    class Config:
        json_schema_extra = {
            "example": {
                "type": "link",
                "content": "https://g1.globo.com/politica/noticia/2024/02/09/video-reuniao-bolsonaro-ministros-golpe-de-estado.ghtml"
            }
        }