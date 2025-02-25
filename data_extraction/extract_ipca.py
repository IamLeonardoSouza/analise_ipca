import requests
import pandas as pd
from datetime import datetime


class IPCAExtractor:
    # URL da API do Banco Central para IPCA
    API_URL  = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10844/dados?formato=json"

    def __init__(self):
        self.data = None

    def fetch_data(self):
        print("🔄 Coletando dados do IPCA...")
        response = requests.get(self.API_URL)
        if response.status_code == 200:
            self.data = response.json()
        else:
            raise Exception(f"Erro ao coletar dados: {response.status_code}")

    def to_dataframe(self):
        if self.data:
            df = pd.DataFrame(self.data)  # Apenas isso!
            return df
        else:
            raise Exception("Nenhum dado para converter em DataFrame")
