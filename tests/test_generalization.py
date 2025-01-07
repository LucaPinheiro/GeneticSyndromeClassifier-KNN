from sklearn.neighbors import KNeighborsClassifier
from src.models.knn_metrics import calculate_metrics
from sklearn.model_selection import train_test_split
import joblib

def test_generalization_with_saved_model(X, y, model_path='models/best_knn_final.pkl'):
    """Teste de Generalização usando o modelo salvo (.pkl)"""
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    knn = joblib.load(model_path)
    print("\n--- Modelo carregado do arquivo .pkl ---")

    print("\n--- Avaliação no Conjunto de Validação ---")
    val_metrics = calculate_metrics(knn, X_val, y_val)
    print(val_metrics)

    print("\n--- Avaliação no Conjunto de Teste ---")
    test_metrics = calculate_metrics(knn, X_test, y_test)
    print(test_metrics)

    return val_metrics, test_metrics
