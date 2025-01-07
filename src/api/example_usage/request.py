
import requests

url = "http://localhost:8000/predict/"
payload = {
    "embedding": [0.1] * 320 
}
response = requests.post(url, json=payload)
print(response.json())


#rode como main enquanto roda o servidor
