from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import delta.tables as dt
from delta import *
import time

class IPCAProcessor:
    def __init__(self):
        print("Iniciando a sessão Spark...")
        self.spark = SparkSession.builder \
            .appName("IPCA Processor") \
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
            .config("spark.jars.packages", "io.delta:delta-core_2.12:1.2.1") \
            .getOrCreate()
        print("Sessão Spark criada com sucesso!")

    def process(self, df):
        print("🔄 Processando dados...")
        df_spark = self.spark.createDataFrame(df)  # Agora pode acessar self.spark corretamente
        df_spark = df_spark.withColumn("valor", col("valor").cast("float"))
        return df_spark

    def save_to_delta(self, df_spark, path=r"delta_tables\ipca"):
        print("💾 Salvando dados no Delta Lake...")
        df_spark.write.format("delta").mode("overwrite").save(path)
