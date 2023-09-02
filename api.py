# api.py
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post('/predict/')
async def predict(data: dict):
    # Simulez une prédiction ici
    response_data = {"result": "Prédiction effectuée avec succès", "data": data}
    return response_data  # Assurez-vous que la réponse est un dictionnaire JSON valide
