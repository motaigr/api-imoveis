from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

@app.get("/calcular")
def calcular(bairro: str, area: float, quartos: int):
    resposta = httpx.get("http://127.0.0.1:8000/valor-m2", params={"bairro": bairro})
    if resposta.status_code != 200:
        raise HTTPException(status_code=404, detail="Bairro não encontrado")
    dados = resposta.json()
    valor_m2 = dados["valor_m2"]
    fator_quartos = 1.0 + (quartos - 2) * 0.05
    preco = area * valor_m2 * fator_quartos
    return {"bairro": bairro, "area": area, "quartos": quartos, "preco_sugerido": preco}

@app.get("/valor-m2")
def calcular_valor_m2(bairro: str):
    valores_m2 = {
        "Centro": 10000,
        "Batel": 12000,
        "Agua Verde": 11000,
        "Novo Mundo": 8000,
        "Pinheirinho": 7000,
        "Cajuru": 10000
    }

    if bairro not in valores_m2:
        raise HTTPException(status_code=404, detail="Bairro não encontrado")
    valor_m2 = valores_m2[bairro]
    return {"bairro": bairro, "valor_m2": valor_m2}

