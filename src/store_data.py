from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def store_data_in_delta(data_frame, delta_path):
    # Inicia a sessão do Spark
    spark = SparkSession.builder.appName("IPCA Analysis").getOrCreate()
    
    # Converte o DataFrame do Pandas para DataFrame do Spark
    spark_df = spark.createDataFrame(data_frame)

    # Salva no Delta Lake
    spark_df.write.format("delta").mode("overwrite").save(delta_path)
    
    print(f"Dados armazenados no Delta Lake em {delta_path}")
