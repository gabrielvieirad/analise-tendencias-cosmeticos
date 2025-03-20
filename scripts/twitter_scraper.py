import tweepy
import logging
import pandas as pd
import os
import re
import time
from collections import Counter

# Configurar logging
logging.basicConfig(level=logging.WARNING, format="%(message)s")

# Criar a pasta 'data/' se não existir
if not os.path.exists("data"):
    os.makedirs("data")

# Chave da API do Twitter (substitua pela sua)
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAO5A0AEAAAAAliAokrynPMWkYs5mivzSPk75kbw%3D5Jw7E7B6j8iRU0wbho9N4pr3X2Z2fUszuQtqpyQlqSHVeZcRUQ"

# Configurar autenticação na API do Twitter
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Controle de tempo limite
tempo_inicio = time.time()
tempo_maximo = 30  # Se após 30 segundos ainda houver erro, o programa encerra


# Função para coletar tweets respeitando os limites da API
def coletar_tweets(query, max_tweets=100):
    tentativa = 1
    while tentativa <= 5:  # Tentar até 5 vezes antes de desistir
        try:
            # Se o tempo de execução ultrapassar 30 segundos, encerra o programa
            if time.time() - tempo_inicio > tempo_maximo:
                logging.warning("Tempo limite de 30 segundos atingido. Encerrando o programa.")
                exit()

            tweets_data = []
            response = client.search_recent_tweets(
                query=f"{query} lang:pt",
                tweet_fields=["created_at", "public_metrics"],
                max_results=min(max_tweets, 100)
            )

            if response.data:
                for tweet in response.data:
                    tweets_data.append({
                        "ID": tweet.id,
                        "Texto": tweet.text,
                        "Data": tweet.created_at,
                        "Curtidas": tweet.public_metrics["like_count"],
                        "Retweets": tweet.public_metrics["retweet_count"]
                    })

            return tweets_data

        except tweepy.errors.TooManyRequests:
            espera = 10 * tentativa  # Começa com 10s e aumenta a cada tentativa
            logging.warning(f"Erro 429 - Muitas requisições. Aguardando {espera} segundos antes de tentar novamente...")
            time.sleep(espera)
            tentativa += 1

        except Exception as e:
            logging.warning(f"Erro ao coletar tweets: {e}")
            return []

    logging.warning("Falha ao coletar tweets após várias tentativas.")
    return []

# Lista de palavras-chave relacionadas a produtos cosméticos
palavras_chave = ["batom", "perfume", "hidratante", "base", "shampoo", "condicionador", "protetor solar"]

# Coletar tweets para cada palavra-chave respeitando os limites da API
todos_tweets = []
for palavra in palavras_chave:
    tweets = coletar_tweets(palavra, max_tweets=5)  # Reduzimos para evitar bloqueio
    todos_tweets.extend(tweets)
    time.sleep(5)  # Aguarda 5 segundos entre cada requisição para não ultrapassar o limite

# Criar DataFrame
df_twitter = pd.DataFrame(todos_tweets)

# Se o DataFrame estiver vazio, evitar erro
if df_twitter.empty:
    logging.warning("Nenhum tweet coletado. Verifique a API do Twitter ou os limites de requisição.")
else:
    # Analisar hashtags mais mencionadas
    def extrair_hashtags(texto):
        return re.findall(r"#\w+", texto)

    df_twitter["Hashtags"] = df_twitter["Texto"].apply(extrair_hashtags)

    # Contar as hashtags mais usadas
    hashtags_todas = [hashtag.lower() for hashtags in df_twitter["Hashtags"] for hashtag in hashtags]
    hashtags_mais_usadas = Counter(hashtags_todas).most_common(10)

    # Salvar os tweets coletados
    csv_path = "data/twitter_data.csv"
    df_twitter.to_csv(csv_path, index=False)

    # Salvar as hashtags mais usadas
    hashtags_df = pd.DataFrame(hashtags_mais_usadas, columns=["Hashtag", "Frequência"])
    hashtags_df.to_csv("data/twitter_hashtags.csv", index=False)

    logging.info(f"Scraping do Twitter finalizado! Dados salvos em {csv_path} e data/twitter_hashtags.csv")
