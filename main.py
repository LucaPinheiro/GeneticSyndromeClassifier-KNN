import numpy as np
import pandas as pd
from src.utils.predict import predict_single_embedding
from tests.test_generalization import test_generalization_with_saved_model

df = pd.read_csv('./data/processed/normalized_data.csv')
X = df.iloc[:, 3:].values
y = df['syndrome_id'].values

# Teste de generalização
test_generalization_with_saved_model(X, y, model_path='./src/models/best_knn_cosine.pkl')

# Simulação de um novo vetor de 320 dimensões
new_embedding = np.random.rand(320)  # Teste com um vetor random

# previsão usando o modelo
predicted_class = predict_single_embedding(new_embedding, model_path='./src/models/best_knn_cosine.pkl')
print(f"A síndrome predita para este novo dado é: {predicted_class}")