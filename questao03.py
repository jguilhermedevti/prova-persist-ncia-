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




