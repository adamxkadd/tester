# api.py
import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post('predict/')
async def predict(data: dict):
    # Simulez une prédiction ici
    prediction = {"result": "Prédiction effectuée avec succès", "data": data}
    return prediction
