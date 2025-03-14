# Análise de Tendências de Cosméticos e Produtos

Este projeto tem como objetivo analisar as tendências de cosméticos e produtos de beleza com base em redes sociais (TikTok, Instagram) e buscas no Google Trends. Além disso, utilizamos **Web Scraping** para coletar preços e descrições de marketplaces como **Amazon, Beleza na Web e Droga Raia**.

---

## Funcionalidades

**Coleta de Dados**  
- Web Scraping de **TikTok e Instagram** para capturar postagens virais.  
- Extração de preços e descrições de produtos de **marketplaces**.  
- Integração com **Google Trends** para análise de popularidade.  

**Análise de Tendências**  
- Processamento de dados para identificar produtos em alta.  
- Uso de **Processamento de Linguagem Natural (NLP)** para categorizar produtos.  
- Predição de demanda futura.  

**Visualização Interativa**  
- Dashboard em **Streamlit** para exibir tendências de mercado.  
- Relatórios sobre comportamento de consumo.  

---

## Estrutura do Projeto

/analise-tendencias-cosmeticos
├── data/  # Armazenar os dados coletados
├── scraping/  # Scripts de Web Scraping
│   ├── tiktok_scraper.py
│   ├── instagram_scraper.py
│   ├── marketplaces_scraper.py
├── analysis/  # Scripts de análise de dados
│   ├── trends_analysis.py
│   ├── sales_forecast.py
├── visualization/  # Dashboards e relatórios
│   ├── dashboard.py
├── main.py  # Script principal do projeto
├── requirements.txt  # Arquivo com dependências
├── README.md  # Documentação do projeto

---

## Tecnologias Utilizadas

- **Linguagem:** Python 
- **Web Scraping:** `Selenium`, `BeautifulSoup`, `Instaloader`
- **Análise de Dados:** `pandas`, `numpy`, `scikit-learn`
- **NLP:** `spaCy`, `NLTK`
- **Visualização:** `Streamlit`, `Plotly`
- **Integração com Google Trends:** `pytrends`

---

## Como Executar o Projeto

1️⃣ Clone este repositório:
```bash
git clone https://github.com/gabrielvieirad/analise-tendencias-cosmeticos.git
cd analise-tendencias-cosmeticos
```
2️⃣ Crie um ambiente virtual e instale as dependências:
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt

3️⃣ Execute os scripts de coleta de dados:
python scraping/tiktok_scraper.py
python scraping/instagram_scraper.py
python scraping/marketplaces_scraper.py

4️⃣ Analise os dados e visualize as tendências:
python analysis/trends_analysis.py
streamlit run visualization/dashboard.py

## Contribuindo
Faça um fork do repositório.
Crie uma branch para sua feature (git checkout -b minha-feature).
Faça o commit das suas mudanças (git commit -m "Adiciona nova feature").
Faça um push para a branch (git push origin minha-feature).
Abra um Pull Request.
