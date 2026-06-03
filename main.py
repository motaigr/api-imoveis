from fastapi import FastAPI, HTTPException

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/calcular")
def calcular(bairro: str, area: float, quartos: int, vagas: int):
    resultado = calcular_valor_m2(bairro)
    valor_m2 = resultado["valor_m2"]
    fator_quartos = 1.0 + (quartos - 2) * 0.05
    fator_vagas = 1.0 + vagas * 0.03
    preco = area * valor_m2 * fator_quartos * fator_vagas
    preco_m2 = preco / area
    return {"bairro": bairro, "area": area, "quartos": quartos, "vagas": vagas, "preco_sugerido": preco, "preco_m2": preco_m2}

@app.get("/valor-m2")
def calcular_valor_m2(bairro: str):
    bairro = bairro.title()
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

