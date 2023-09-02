# api.py
from fastapi import FastAPI
from pydantic import BaseModel
import json



app = FastAPI()

class InputData(BaseModel):
    msg: str

@app.post("/hello")
def read_root(input_data: InputData):
    result = json.loads(r'[{"id": 1}, {"id": 2}]')
    return {result}
