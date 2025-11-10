import pandas as pd
from fastapi import FastAPI

app = FastAPI()
dados_pessoas = {
    'id': [1, 2, 3, 4, 5],
    'nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa'],
    'idade': [23, 30, 25, 41, 28],
    'cidade': ['São Paulo', 'Recife', 'Salvador', 'Manaus', 'Recife']
}
tabela_pessoas = pd.DataFrame(dados_pessoas)

@app.get("/pessoas")
def obter_pessoas():
    # Retorna o DataFrame full em JSON
    return tabela_pessoas.to_dict("records")


@app.get("/pessoas/{cidade}")
def obter_pessoas_por_cidade(cidade: str):
    # Filtra a tabela pela cidade 
    filtro = tabela_pessoas['cidade'].str.lower() == cidade.lower()
    resultado = tabela_pessoas[filtro]
    
    # Retorna os dados filtrados como JSON
    return resultado.to_dict("records")
