
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY src/models/best_knn_cosine.pkl /app/src/models/best_knn_cosine.pkl

