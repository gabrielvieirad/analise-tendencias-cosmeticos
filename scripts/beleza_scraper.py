import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os

# Configurar logging
logging.basicConfig(level=logging.WARNING, format="%(message)s")

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
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")  # Disfarçar Selenium

# Iniciar o driver do Chrome
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# URL dos mais vendidos na Beleza na Web
beleza_url = "https://www.belezanaweb.com.br/mais-vendidos/"

logging.info("Acessando Beleza na Web...")
driver.get(beleza_url)

# Tempo de espera máximo
max_wait_time = 15

# Imprimir o HTML capturado para verificar se a página carregou corretamente
time.sleep(5)  # Esperar um pouco antes de capturar o HTML
html_content = driver.page_source
with open("debug_belezanaweb.html", "w", encoding="utf-8") as f:
    f.write(html_content)
logging.warning("Página salva em debug_belezanaweb.html. Verifique se os produtos estão visíveis.")

# Tentar encontrar os produtos
try:
    WebDriverWait(driver, max_wait_time).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.showcase-item-title"))
    )
    logging.info("Produtos carregados.")
except:
    logging.warning("Os produtos não carregaram a tempo.")
    driver.quit()
    exit()

# Fazer múltiplos scrolls para carregar todos os produtos
for _ in range(3):
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(2)

# Capturar os produtos na página dos mais vendidos
products_beleza = driver.find_elements(By.CSS_SELECTOR, "a.showcase-item-title")
logging.info(f"Produtos encontrados na Beleza na Web: {len(products_beleza)}")

data_beleza = []
for product in products_beleza[:20]:  # Limitar a 20 produtos para teste
    try:
        # Capturar o nome do produto
        try:
            name = product.text.strip()
        except:
            name = "Nome não encontrado"

        # Capturar o link do produto
        try:
            link = product.get_attribute("href")
        except:
            link = "Link não encontrado"

        # Capturar o preço do produto
        try:
            price_element = product.find_element(By.XPATH, ".//following::span[@class='price-value'][1]")
            price = price_element.text.strip() if price_element else "Preço não encontrado"
        except:
            price = "Preço não encontrado"

        logging.debug(f"Produto: {name} - {price}")
        data_beleza.append({"Nome": name, "Preço": price, "Link": link})
    except Exception as e:
        logging.warning(f"Erro ao coletar um produto: {e}")
        continue

# Salvar os dados em CSV
df_beleza = pd.DataFrame(data_beleza)
csv_path = "data/beleza_products.csv"

if not df_beleza.empty:
    df_beleza.to_csv(csv_path, index=False)
    logging.info(f"Scraping da Beleza na Web finalizado! Dados salvos em {csv_path}")
else:
    logging.warning("Nenhum dado encontrado na Beleza na Web.")

# Fechar o navegador
driver.quit()
