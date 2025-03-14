from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Caminho do Opera GX (ajuste se necessário)
opera_path = "C:\\Program Files\\Opera GX\\opera.exe"
opera_driver_path = "operadriver.exe"

# Configuração do WebDriver para Opera
options = webdriver.ChromeOptions()
options.binary_location = opera_path

driver = webdriver.Opera(executable_path=opera_driver_path, options=options)

# Url de busca na Amazon (exemplo:maquiagem)
search_query = "maquiagem"
amazon_url = f"https://www.amazon.com.br/s?k={search_query}"

# Acessa a página da Amazon
driver.get(amazon_url)
time.sleep(3) # Aguarda carregamento

# Coleta os dados do produtos
products = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div.s-result-item")

data = []
for product in products[:20]: # Coletar os primeiros 10 produtos
    try:
        name = product.find_element(By.CSS_SELECTOR, "h2 a span").text
        price = product.find_element(By.CSS_SELECTOR, ".a-price-whole").text
        link = product.find_element(By.CSS_SELECTOR, "h2 a").get_attribute("href")
        data.append({"Nome": name, "Preço": price, "Link": link})
    except:
        continue

# Salva os dados em um DataFrame
df = pd.DataFrame(data)
df.to_csv("data/amazon_products.csv", index=False)

print("Scraping finalizado! Dados salvos em data/amazon_products.csv.")

# Fecha o navegador
driver.quit()