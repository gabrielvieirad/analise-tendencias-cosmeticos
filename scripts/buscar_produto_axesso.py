import requests

RAPIDAPI_KEY = "SUA_CHAVE_AXESSO_AQUI"

def buscar_produto_ean(ean):
    url = "https://amazon-data-service.p.rapidapi.com/request"

    querystring = {
        "search_term": ean,
        "domainCode": "br",  # amazon.com.br
        "page": "1",
        "type": "search"
    }

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "amazon-data-service.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()

        if not data.get("searchResults"):
            print("❌ Nenhum produto encontrado.")
            return []

        print("✅ Produto(s) encontrado(s):\n")

        for produto in data["searchResults"][:1]:  # Apenas o primeiro
            nome = produto.get("title")
            preco = produto.get("price")
            link = produto.get("productUrl")
            imagem = produto.get("imageUrl")

            print(f"Nome: {nome}")
            print(f"Preço: {preco}")
            print(f"Link: {link}")
            print(f"Imagem: {imagem}")
            print("-" * 50)

        return data["searchResults"]

    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
        return []

if __name__ == "__main__":
    codigo = input("Digite o código de barras (EAN/GTIN/UPC): ").strip()
    buscar_produto_ean(codigo)
