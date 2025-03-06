import requests
import json
import os

def collect_ipca_data():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10844/dados?formato=json&dataInicial=01/01/1995&dataFinal=01/01/2025"
    response = requests.get(url)
    
    if response.status_code == 200:
        ipca_data = response.json()
        print(f"{len(ipca_data)} dados coletados com sucesso!")
        
        # Salva os dados em um arquivo JSON
        output_path = os.path.join("data/raw/ipca_data.json")
        with open(output_path, "w") as f:
            json.dump(ipca_data, f, indent=4)
        
        return ipca_data
    else:
        print(f"Erro na requisição: {response.status_code}")
        return None
