import os
from src.collect_data import collect_data
from src.process_data import process_data
from notebooks.ipca_processing_notebook import collect_and_store_ipca

def main():
    # Etapa 1: Coletar os dados
    print("Coletando os dados do IPCA...")
    collect_data()

    # Etapa 2: Processar os dados
    print("Processando os dados do IPCA...")
    process_data()

    # Etapa 3: Armazenar em Delta Lake
    print("Armazenando os dados em Delta Lake...")
    collect_and_store_ipca()

    print("Execução concluída!")

if __name__ == "__main__":
    main()
