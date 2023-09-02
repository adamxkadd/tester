# api.py
import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post('/ppredict/')
async def predict(data: dict):
    # Simulez une prédiction ici
    reponse = {"result": "reponse effectuée avec succès", "data": data}
    return reponse
