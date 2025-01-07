# 📦 Projeto de Classificação de Síndromes Genéticas

Este projeto visa concluir o teste de classificação de síndromes genéticas a partir de embeddings de imagens utilizando o algoritmo **K-Nearest Neighbors (KNN)**. A abordagem inclui pré-processamento de dados, visualização exploratória, treinamento de modelo e avaliação de métricas de desempenho.

## 📊 **Objetivos do Projeto:**
- **Classificar síndromes genéticas** usando embeddings de imagens.  
- Realizar **Análise Exploratória de Dados (EDA)**.  
- Implementar o algoritmo **KNN** com otimização de hiperparâmetros.  
- Avaliar o modelo usando **F1-Score, AUC e Top-3 Accuracy**.  

---

## 📁 **Estrutura de Pastas:**

```plaintext
project
├── data/
│   ├── raw/ (Dados brutos .p)
│   ├── processed/ (Dados normalizados)
│   └── results/ (Métricas e gráficos gerados)
│
├── src/
│   ├── data_processing/ (Carregamento e normalização de dados)
│   ├── visualization/ (Scripts de visualização de EDA e t-SNE)
│   ├── models/ (Implementação do KNN e métricas)
│   └── utils/ (Funções auxiliares)
│
├── tests/ (Testes)
├── main.py (Pipeline principal)
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ **Instalação e Configuração:**

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-repo/ml_pipeline_project.git
   ```
2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # (Linux/Mac)
   .venv\Scripts\activate  # (Windows)
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📈 **Como Executar o Projeto:**
1. **Pré-processamento:** Executar o arquivo `main.py` para carregar e normalizar os dados.
2. **Treinamento:** Realizar o treinamento do modelo KNN usando `src/models/knn_classifier.py`.
3. **Avaliação:** Verificar as métricas usando `src/models/knn_metrics.py` e rodando no main.
4. **Visualização:** Execute `src/visualization/eda_analysis.py` para gerar gráficos como t-SNE.

---

## 🧪 **Testes:**
- Testes estão na pasta `tests/`.  
- Para rodar os testes:  rode o main
```

---

## 📊 **Resultados Principais:**
- **F1-Score:** 0.86
- **AUC:** 0.98
- **Top-3 Accuracy:** 95%

---

