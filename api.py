# api.py
import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post('predict/')
async def predict(data: dict):
    # Simulez une prédiction ici
    print("La fonction predict a débuté son exécution.")

    reponse = {"result": "reponse effectuée avec succès", "data": data}
    return reponse
