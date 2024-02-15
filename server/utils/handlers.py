import os
import requests
from numpy import argmax
from dotenv import load_dotenv
from fastapi import HTTPException
from starlette import status

load_dotenv()

class CustomRequestHandler:
    def __init__(self, raw_text) -> None:
        self.raw_text: str = raw_text
        self._API_URL = "https://api-inference.huggingface.co/models/alvarophylipe/portuguese-fake-news-classification"
        self._HEADERS = {
            "Authorization": f"Bearer {os.getenv('API_KEY')}"
        }
        self.query_response = self._query()
    
    def _query(self):
        response = requests.post(self._API_URL, headers=self._HEADERS, json=self._generate_payload())
        return response.json()


    def _get_limit_text(self, text) -> str:
        tokens = text.split()
        return " ".join([tokens[i] for i in range(len(tokens)) if i < 300])
    

    def _generate_payload(self) -> dict:
        return {
            "inputs": self._get_limit_text(self.raw_text)
        }
    
    def _get_prediction(self):
        items = {item.get('label'):item.get('score') for item in self.query_response[0]}
        predictions = [value[1] for value in sorted(items.items())]
        return {"prediction": int(argmax(predictions))}


    def get_result(self):
        try:
            result = self._get_prediction()
        except:
            estimated_time = self.query_response.get('estimated_time')
            if estimated_time:
                return {
                    'estimated_time': estimated_time
                }
            else:
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
    
