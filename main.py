from fastapi import FastAPI
from src.api.controller.prediction_controller import predict_endpoint

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API de Previsão de Síndrome com FastAPI está rodando!"}

app.include_router(predict_endpoint)


