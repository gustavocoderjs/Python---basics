

from fastapi import FastAPI 

app = FastAPI()

vendas = { 
           1: {"item": "lata", "preco_unit": 4, "quantidade": 5},
           2: {"item": "garrafa", "preco_unit": 12, "quantidade": 3},
           3: {"item": "drink", "preco_unit": 7, "quantidade": 2},
}

 
@app.get("/")
def home():
    return {"Vendas": len(vendas)} 

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else: 
        return {"Erro": "ID da Venda não existe!"}
    
    



