import joblib
import numpy as np

def predict_single_embedding(embedding, model_path='models/best_knn_cosine.pkl'):
    model = joblib.load(model_path)
    
    embedding_array = np.array(embedding).reshape(1, -1)
    
    prediction = model.predict(embedding_array)
    
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(embedding_array)
        top_3_classes = np.argsort(probabilities[0])[-3:][::-1]
        print(f"Top-3 Classes: {top_3_classes}")
        print(f"Probabilidades: {probabilities[0][top_3_classes]}")
    
    print(f"Predição: {prediction[0]}")
    return prediction[0]
