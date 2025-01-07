from fastapi import APIRouter
from pydantic import BaseModel
import joblib
import numpy as np

predict_endpoint = APIRouter()

model = joblib.load("src/models/best_knn_cosine.pkl")

class EmbeddingSchema(BaseModel):
    embedding: list[float]

@predict_endpoint.post("/predict/")
def predict(data: EmbeddingSchema):
    try:
        if len(data.embedding) != 320:
            return {"error": "O vetor de entrada deve ter exatamente 320 dimensões."}

        input_array = np.array(data.embedding).reshape(1, -1)
        predicted_class = model.predict(input_array)[0]

        return {
            "predicted_class": int(predicted_class),
            "message": "Previsão realizada com sucesso!"
        }
    except Exception as e:
        return {"error": str(e)}
