from fastapi import FastAPI
import uvicorn
from src.api.controller.prediction_controller import predict_endpoint

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API de Previsão de Síndrome com FastAPI está rodando!"}

app.include_router(predict_endpoint)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
