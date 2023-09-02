# api.py
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post('/predict/')
async def predict(data: dict):
    response_data = {"result": "Prédiction effectuée avec succès", "data": data}
    return JSONResponse(content=response_data)
