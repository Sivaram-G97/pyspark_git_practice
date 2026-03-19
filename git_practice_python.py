from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("GitPractice").getOrCreate()
data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])
df = spark.createDataFrame(data, schema)

df.info()
df.withColumn("department")
