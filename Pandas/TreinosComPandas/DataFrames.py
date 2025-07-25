import pandas as pd
dados = {
    "nome": ["Ana", "Bruno", "Carla", "Daniel"],
    "idade": [23, 35, 29, 42],
}

df = pd.DataFrame(dados)
print(df)