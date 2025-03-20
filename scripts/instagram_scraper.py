import requests
import pandas as pd
import os 

# Criar a pasta "data/" se não existir 
if not os.path.exists("data"):
    os.makedirs("data")


# Configurar Token de Acesso e ID do Usuário do Instagram
ACCESS_TOKEN = "ACESS_TOKEN"
USER_ID = "USER_ID" # Pode ser obtido na API do Facebook Graph

# URL base da API do Instagram 
BASE_URL = f"https://graph.instagram.com/{USER_ID}/media"

# Parâmetros de requisição 
params = {
    "fields":"id, caption, media_type, media_url, timestamp",
    "access_token": ACCESS_TOKEN
}

# Fazer a requisição 
response = requests.get(BASE_URL, params=params)

# Verificar se a resposta foi bem-sucedida
if response.status_code == 200:
    data = response.json()["data"]

    # Criar DataFrame e salvar
    df_instagram = pd.DataFrame(data)
    df_instagram.to_csv("data/instagram_data.csv", index=False)

    print("Coleta do Instagram finalizada! Dados salvos em data/instagram_data.csv")

else:
    print(f"Erro ao coletar dados do Instagram: {response.status_code} - {response.text}")
    
