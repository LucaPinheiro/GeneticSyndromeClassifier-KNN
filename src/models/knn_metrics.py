from sklearn.metrics import f1_score, roc_auc_score, top_k_accuracy_score

def calculate_metrics(model, X_test, y_test, k=3):
    
    y_pred = model.predict(X_test)

    # F1-Score
    f1 = f1_score(y_test, y_pred, average='weighted')

    # Calcula AUC
    # -- Vi em doc / gpt isso, fiquei um pouco com d[uvida nessa métrica, não vou negar
    if hasattr(model, "predict_proba"):
        y_proba = model.predict_proba(X_test)
        auc = roc_auc_score(y_test, y_proba, multi_class='ovr')
    else:
        auc = "N/A (Proba not available)"
    
    # Top-K Accuracy
    if hasattr(model, "predict_proba"):
        top_k_acc = top_k_accuracy_score(y_test, y_proba, k=k)
    else:
        top_k_acc = "Não válida para este modelo"
    
    # print dos resultados
    print(f"F1-Score: {f1:.4f}")
    print(f"AUC: {auc}")
    print(f"Top-{k} Accuracy: {top_k_acc}")

    # Retornar os resultados e em um futuro pode ser salvo
    return {
        "F1-Score": f1,
        "AUC": auc,
        f"Top-{k} Accuracy": top_k_acc
    }
