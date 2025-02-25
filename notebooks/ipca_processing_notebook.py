import requests
import pandas as pd
from pyspark.sql import SparkSession
from io import StringIO
import json


def collect_and_store_ipca():
    # URL da API
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10844/dados?formato=json&dataInicial=01/01/1995&dataFinal=01/01/2025"
    
    # Requisição dos dados
    response = requests.get(url)
    
    # Carregar os dados em um DataFrame pandas
    data = StringIO(response.text)
    df = pd.read_csv(data, sep=";", header=None, names=["Data", "IPCA"])
    
    # Converter a coluna 'Data' para datetime
    df['Data'] = df['Data'].apply(lambda x: json.loads(x) if isinstance(x, str) else x)

    # Criar uma sessão do Spark
    spark = SparkSession.builder \
        .appName("IPCA Processing") \
        .config("spark.jars.packages", "io.delta:delta-core_2.12:1.0.0") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .getOrCreate()

    # Converter o DataFrame pandas para DataFrame Spark
    df_spark = spark.createDataFrame(df)
    
    # Armazenar os dados em Delta Lake
    df_spark.write.format("delta").save(r"data\ipca")

    # Exibir as primeiras linhas
    df_spark.show()
