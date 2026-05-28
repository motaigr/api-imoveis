# API de Precificação de Imóveis

API REST desenvolvida em Python com FastAPI para sugerir preços de imóveis com base no bairro, área e número de quartos.

## Tecnologias
- Python
- FastAPI
- httpx
- Uvicorn

## Como rodar localmente

1. Clone o repositório:
   git clone https://github.com/motaigr/api-imoveis.git

2. Crie e ative o ambiente virtual:
   python -m venv venv
   venv\Scripts\activate

3. Instale as dependências:
   pip install -r requirements.txt

4. Inicie o servidor:
   uvicorn main:app --reload

5. Acesse a documentação em: http://127.0.0.1:8000/docs

## Endpoints

### GET /calcular
Retorna o preço sugerido de um imóvel.

Parâmetros: bairro, area, quartos

Exemplo de resposta:
{
  "bairro": "Batel",
  "area": 80,
  "quartos": 3,
  "preco_sugerido": 1008000.0
}

### GET /valor-m2
Retorna o valor do metro quadrado de um bairro.

Parâmetros: bairro

Exemplo de resposta:
{
  "bairro": "Batel",
  "valor_m2": 12000
}

## 🌐 Demo

Documentação da API: [api-imoveis-prpm.onrender.com/docs](https://api-imoveis-prpm.onrender.com/docs)

## 🔗 Frontend

Interface conectada a esta API: [front-skip.vercel.app](https://front-skip.vercel.app)