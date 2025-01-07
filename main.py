from fastapi import FastAPI
from src.api.controller.prediction_controller import predict_endpoint
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API de Previsão de Síndrome com FastAPI está rodando!"}

app.include_router(predict_endpoint)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000)) 
    uvicorn.run("main:app", host="0.0.0.0", port=port)
