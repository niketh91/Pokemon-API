from pyspark import SparkSession
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

#Create spark session
spark = SparkSession.builder.appName("bronze_schema").getOrCreate()

#Azure Credentials
ACCOUNT_NAME = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
CONTAINER_NAME = os.getenv("CONTAINER")
FOLDER_NAME = os.getenv("FOLDER") #landing

#ADLS source path and bronze folder (target) path
source_path = f"abfss://{CONTAINER_NAME}@{ACCOUNT_NAME}.dfs.core.windows.net/{FOLDER_NAME}/"
bronze_path = f"abfss://{CONTAINER_NAME}@{ACCOUNT_NAME}.dfs.core.windows.net/bronze/"

#Read CSV from ADLS
pokemon_df = spark.read.option("header", "True").csv(f"{source_path}pokemon.csv")

#Write df to bronze path
pokemon_df.write.format("delta").mode("overwrite").save(f"{bronze_path}pokemon")

#Create table
spark.sql(f"""
        CREATE TABLE IF NOT EXISTS bronze_pokemon
        USING DELTA
        LOCATION '{bronze_path}pokemon'     
""")