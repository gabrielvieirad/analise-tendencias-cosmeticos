import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def buscar_produto(term_busca):
    """
    Busca um produto na Amazon usando undetected-chromedriver.
    Retorna nome, preço, avaliação e link do primeiro resultado.
    """

    options = uc.ChromeOptions()

    # Evita detecção
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")

    # (Opcional) user-agent personalizado
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")

    try:
        driver = uc.Chrome(options=options, headless=False)  # headless=False para testes

        driver.get("https://www.amazon.com.br/ref=nav_logo")

        # Espera a barra de busca carregar
        barra_pesquisa = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        barra_pesquisa.send_keys(term_busca)
        barra_pesquisa.send_keys(Keys.RETURN)

        # Espera os resultados aparecerem
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot"))
        )

        html = driver.page_source
        with open("pagina_amazon.html", "w", encoding="utf-8") as f:
            f.write(html)

        input("HTML da página salvo. Pressione ENTER para sair.")


        produtos = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")

        resultados = []
        for produto in produtos:
            try:
                nome = produto.find_element(By.CSS_SELECTOR, "h2 a span").text
                link = produto.find_element(By.CSS_SELECTOR, "h2 a").get_attribute("href")
                preco = produto.find_element(By.CSS_SELECTOR, ".a-price-whole").text
                avaliacao = produto.find_element(By.CSS_SELECTOR, ".a-icon-alt").text

                resultados.append({
                    "nome": nome,
                    "preco": preco,
                    "avaliacao": avaliacao,
                    "link": link
                })
                break  # Só o primeiro válido
            except Exception:
                continue

        return resultados

    except Exception as e:
        print(f"Erro durante a execução: {str(e)}")
        return []
    finally:
        try:
            try:
                html = driver.page_source
                with open("pagina_amazon.html", "w", encoding="utf-8") as f:
                    f.write(html)
                input("HTML salvo. Pressione ENTER para continuar...")
            except Exception as html_error:
                print(f"Erro ao salvar HTML: {html_error}")

            driver.quit()
        except:
            pass

# Execução direta no terminal
if __name__ == "__main__":
    termo = input("Digite o nome do produto ou o código de barras: ").strip()
    resultado = buscar_produto(termo)

    if not resultado:
        print("Nenhum produto encontrado.")
    else:
        print("\nProdutos encontrados:\n")
        for item in resultado:
            print(f"Nome: {item['nome']}")
            print(f"Preço: R${item['preco']}")
            print(f"Avaliação: {item['avaliacao']}")
            print(f"Link: {item['link']}")
            print("-" * 50)
