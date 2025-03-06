import os
from src.collect_data import collect_ipca_data
from src.process_data import process_ipca_data
from src.store_data import store_data_in_delta
from src.generate_reports import generate_ipca_report

def main():
    # Passo 1: Coletar dados
    print("Coletando dados do IPCA...")
    ipca_data = collect_ipca_data()
    
    if not ipca_data:
        print("Erro na coleta de dados. Encerrando o processo.")
        return
    
    # Passo 2: Processar dados
    raw_data_path = r"data\raw\ipca_data.json"
    print("Processando os dados...")
    processed_df = process_ipca_data(raw_data_path)
    
    # Passo 3: Armazenar dados no Delta Lake
    delta_path = "/mnt/delta/ipca_data"
    print("Armazenando dados no Delta Lake...")
    store_data_in_delta(processed_df, delta_path)
    
    # Passo 4: Gerar relatórios e gráficos
    processed_data_path = r"data\processed\ipca_processed.csv"
    print("Gerando relatório e gráficos...")
    generate_ipca_report(processed_data_path)
    
    print("Processo concluído com sucesso!")

if __name__ == "__main__":
    main()
