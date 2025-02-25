import requests
import os

def collect_data():
    # URL da API do Banco Central
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10844/dados?formato=json&dataInicial=01/01/1995&dataFinal=01/01/2025"

    # Fazer a requisição GET
    response = requests.get(url)

    # Garantir que o diretório de dados exista
    if not os.path.exists("data"):
        os.makedirs("data")

    # Salvar os dados em um arquivo CSV
    with open("data/ipca.csv", "wb") as file:
        file.write(response.content)

    print("Dados coletados com sucesso!")
