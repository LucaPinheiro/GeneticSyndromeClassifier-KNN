import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_valid_embedding():
    response = client.post(
        "/predict/",
        json={"embedding": [0.1] * 320}
    )
    assert response.status_code == 200
    assert "predicted_class" in response.json()
    assert response.json()["message"] == "Previsão realizada com sucesso!"

def test_predict_invalid_embedding_length():
    response = client.post(
        "/predict/",
        json={"embedding": [0.1] * 300} 
    )
    assert response.status_code == 200
    assert "error" in response.json()
    assert "O vetor de entrada deve ter exatamente 320 dimensões." in response.json()["error"]

def test_predict_invalid_data_type():
    response = client.post(
        "/predict/",
        json={"embedding": ["invalid_data"] * 320} 
    )
    assert response.status_code == 422  