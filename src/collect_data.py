import requests
import pandas as pd
from loguru import logger

def collect_data():
    # API URL
    data_url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10844/dados?formato=json&dataInicial=01/01/1995&dataFinal=01/01/2025"
    
    # API Request
    response = requests.get(data_url)
    data = response.json()
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Convert the 'date' column to date format
    # Convert the 'value' column to float
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    df['valor'] = df['valor'].str.replace(',', '.').astype(float)
    
    # Save to an Excel file
    df.to_excel(r"data\data_ipca.xlsx", index=False)
    
    logger.success("File saved successfully as 'data_ipca.xlsx'")
