import pyspark
from pyspark.sql import SparkSession

# non-databricks notebooks require the initiation of a spark session.
spark = (SparkSession.builder.getOrCreate())

def tableExists(tableName, dbName):
  return spark.catalog.tableExists(f"{dbName}.{tableName}")

