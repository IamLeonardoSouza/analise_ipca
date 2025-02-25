import pandas as pd
import matplotlib.pyplot as plt

class IPCAVisualizer:
    def __init__(self, df):
        self.df = df

    def plot_ipca_trend(self):
        print("📊 Criando gráfico da variação do IPCA...")
        plt.figure(figsize=(10, 5))
        plt.plot(self.df['ano'], self.df['valor'], marker='o', linestyle='-')
        plt.title("Variação do IPCA ao longo dos anos")
        plt.xlabel("Ano")
        plt.ylabel("IPCA")
        plt.grid(True)
        plt.show()
