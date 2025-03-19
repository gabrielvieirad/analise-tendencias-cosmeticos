from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os

# Criar a pasta 'data/' se não existir
if not os.path.exists("data"):
    os.makedirs("data")

# Caminho do ChromeDriver
chrome_driver_path = "drivers/chromedriver.exe"

# Configuração do WebDriver para Google Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Para rodar sem abrir o navegador
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Iniciar o driver do Chrome
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# URL dos mais vendidos na Amazon
amazon_url = "https://www.amazon.com.br/gp/bestsellers/beauty/ref=zg_bs_nav_beauty_0"

print("Acessando a Amazon...")
driver.get(amazon_url)
time.sleep(5)  # Aguardar carregamento da página

# Capturar os produtos na página dos mais vendidos
products_amazon = driver.find_elements(By.CSS_SELECTOR, "div.p13n-sc-uncoverable-faceout")
print(f"Produtos encontrados na Amazon: {len(products_amazon)}")

data_amazon = []
for product in products_amazon[:20]:  # Limitar a 20 produtos para teste
    try:
        # Capturar o nome do produto
        try:
            name = product.find_element(By.CSS_SELECTOR, "div._cDEzb_p13n-sc-css-line-clamp-3_g3dy1").text
        except:
            name = "Nome não encontrado"

        # Capturar o preço do produto
        try:
            price = product.find_element(By.CSS_SELECTOR, "span._cDEzb_p13n-sc-price_3mJ9Z").text
        except:
            price = "Preço não encontrado"

        # Capturar o link do produto
        try:
            link = product.find_element(By.CSS_SELECTOR, "a.a-link-normal").get_attribute("href")
        except:
            link = "Link não encontrado"

        data_amazon.append({"Nome": name, "Preço": price, "Link": link})
    except Exception as e:
        print(f"Erro ao coletar um produto: {e}")
        continue

# Salvar os dados em CSV
df_amazon = pd.DataFrame(data_amazon)
csv_path = "data/amazon_products.csv"

if not df_amazon.empty:
    df_amazon.to_csv(csv_path, index=False)
    print(f"Scraping da Amazon finalizado! Dados salvos em {csv_path}")
else:
    print("Nenhum dado encontrado na Amazon.")

# Fechar o navegador
driver.quit()
