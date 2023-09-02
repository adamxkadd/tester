# api.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    msg: str

@app.post("/hello")
def read_root(input_data: InputData):
    return {"message": "Hello World"}
