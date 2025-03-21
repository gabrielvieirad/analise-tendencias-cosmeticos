# Análise de Tendências de Cosméticos

Este projeto tem como objetivo **coletar, armazenar e analisar dados sobre produtos cosméticos mais populares** em marketplaces e redes sociais. A análise cruza dados de vendas, redes sociais e buscas no Google para identificar tendências de consumo.

---

## 📦 Funcionalidades

- Scraping de produtos mais vendidos em:
  - [x] Amazon (Beleza)
  - [x] Beleza na Web
- Coleta de dados do Google Trends
- Coleta de dados do Twitter (em desenvolvimento)
- Coleta de dados do Instagram (via Graph API - em desenvolvimento)
- Armazenamento de dados em arquivos `.csv`
- Pronto para integração com Streamlit (dashboard de visualização)

---

## 🛠 Tecnologias

- Python 3
- Selenium
- Pandas
- Pytrends
- Tweepy (Twitter API)
- Meta Graph API (Instagram)
- ChromeDriver

---

## ⚙️ Como executar
1. Clone o repositório:
```bash
git clone https://github.com/gabrielvieirad/analise-tendencias-cosmeticos.git
cd analise-tendencias-cosmeticos
```
2. Instale as dependências:
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt

3. Execute os scripts desejados:
python scripts/amazon_scraper.py
python scripts/beleza_scraper.py
python scripts/google_trends_scraper.py
python scripts/twitter_scraper.py
python scripts/instagram_scraper.py

## 📊 Resultados
Os dados coletados são armazenados em arquivos .csv na pasta /data. Esses arquivos serão utilizados posteriormente para análise e visualização com Streamlit ou outra ferramenta.
---
## 🔐 Notas sobre autenticação
- Para Twitter: é necessário fornecer uma BEARER_TOKEN válida.
- Para Instagram: é necessário ter uma conta comercial e gerar um token via Graph API da Meta.
---
## 🧪 Testes e Validação
Os scripts foram testados localmente com logs de execução. Os scrapers utilizam técnicas de fallback e tratamento de erros para sites dinâmicos.
---
## 📌 Status do Projeto
- Coleta dos marketplaces: ✅ Finalizada
- Google Trends: ✅ Implementado 
- Twitter: ⚠️ Em desenvolvimento (limites de API)
- Instagram: ⚠️ Em fase de autenticação e testes
- Visualização: 🔜 Em breve com Streamlit
---
## 📄 Licença
Este projeto é de uso educacional e experimental. Verifique os termos de uso das APIs e dos sites antes de uso comercial.
---





