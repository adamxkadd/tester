# api.py
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post('/predict/')
async def predict(data: dict):
    # Simulez une prédiction ici
    prediction_result = {"result": "Prédiction effectuée avec succès", "data": data}
    
    # Utilisez JSONResponse pour renvoyer une réponse JSON personnalisée
    return JSONResponse(content=prediction_result)
