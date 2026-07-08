from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

with open("curitiba_imoveis_data.json", "r", encoding="utf-8") as f:
    bairros_data = json.load(f)  # Verifica se o arquivo existe e fecha imediatamente

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/valor-m2")
def calcular_valor_m2(bairro: str, tipo: str = "apartamento"):
    bairro_normalizado = bairro.title()
    
    bairro_info = next((b for b in bairros_data if b["bairro"] == bairro_normalizado), None)
    
    if not bairro_info:
        raise HTTPException(status_code=404, detail="Bairro não encontrado")
    
    campo = f"valor_m2_{tipo}"
    valor_m2 = bairro_info.get(campo)
    
    if valor_m2 is None:
        raise HTTPException(status_code=404, detail=f"Dados de '{tipo}' não disponíveis para este bairro")
    
    return {
        "bairro": bairro_info["bairro"],
        "tipo": tipo,
        "valor_m2": valor_m2,
        "perfil": bairro_info["perfil"],
        "tendencia": bairro_info["tendencia"]
    }

@app.get("/calcular")
def calcular(bairro: str, area: float, quartos: int, vagas: int, tipo: str = "apartamento"):
    resultado = calcular_valor_m2(bairro, tipo)
    valor_m2 = resultado["valor_m2"]
    
    fator_vagas = 1.0 + vagas * 0.03
    
    if tipo == "comercial":
        preco = area * valor_m2 * fator_vagas
    else:
        fator_quartos = 1.0 + (quartos - 2) * 0.05
        preco = area * valor_m2 * fator_quartos * fator_vagas
    
    preco_m2 = preco / area
    return {
        "bairro": bairro,
        "tipo": tipo,
        "area": area,
        "quartos": quartos if tipo != "comercial" else None,
        "vagas": vagas,
        "preco_sugerido": preco,
        "preco_m2": preco_m2,
        "perfil": resultado["perfil"],
        "tendencia": resultado["tendencia"]
    }

