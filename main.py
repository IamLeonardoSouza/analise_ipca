from data_extraction.extract_ipca import IPCAExtractor
from data_processing.process_ipca import IPCAProcessor
from visualization.generate_dashboard import IPCAVisualizer

def main():
    print("🚀 Iniciando pipeline de análise do IPCA...")

    # Extração
    extractor = IPCAExtractor()
    extractor.fetch_data()
    df = extractor.to_dataframe()

    # Processamento
    processor = IPCAProcessor()
    df_spark = processor.process(df)
    processor.save_to_delta(df_spark)

    # Visualização
    visualizer = IPCAVisualizer(df)
    visualizer.plot_ipca_trend()

    print("✅ Pipeline concluído!")

if __name__ == "__main__":
    main()
