import pandas as pd
import json
from datetime import datetime

def process_ipca_data(raw_data_path):
    # Carrega os dados brutos
    with open(raw_data_path, "r") as f:
        data = json.load(f)
    
    # Cria um DataFrame do Pandas
    df = pd.DataFrame(data)
    
    # Converte a coluna 'data' para o formato de data
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    df['valor'] = df['valor'].astype(float)

    # Salva o DataFrame processado
    processed_path = r"data\processed\ipca_processed.csv"
    df.to_csv(processed_path, index=False)
    
    print(f"Dados processados e salvos em {processed_path}")
    return df
