import pandas as pd
import matplotlib.pyplot as plt

def generate_ipca_report(processed_data_path):
    # Carrega os dados processados
    df = pd.read_csv(processed_data_path)
    
    # Geração de um gráfico de linha
    df_grouped = df.groupby(df['data'].dt.year)['valor'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    plt.plot(df_grouped['data'], df_grouped['valor'], marker='o')
    plt.title('Variação Anual do IPCA')
    plt.xlabel('Ano')
    plt.ylabel('Valor do IPCA')
    plt.grid(True)
    plt.savefig(r'data\output\ipca_line_chart.png')
    
    print("Gráfico de linha gerado com sucesso.")
