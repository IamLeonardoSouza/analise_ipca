import pandas as pd
import os
import json

def process_data():
    # Garantir que o arquivo de dados exista
    if not os.path.exists("data/ipca.csv"):
        print("Erro: Arquivo de dados não encontrado!")
        return

    # Carregar os dados
    df = pd.read_csv("data/ipca.csv", sep=";", header=None, names=["Data", "IPCA"])

    # Converter a coluna 'Data' para datetime
    df['Data'] = df['Data'].apply(lambda x: json.loads(x) if isinstance(x, str) else x)

    # Salvar o DataFrame limpo
    df.to_csv("data/processed_ipca.csv", index=False)

    print("Dados processados com sucesso!")
