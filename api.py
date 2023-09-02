# api.py
from fastapi import FastAPI

app = FastAPI()

@app.post("/hello")
def read_root(input=):
    return {"message": "Hello World"}
