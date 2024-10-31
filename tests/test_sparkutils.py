from pyspark.sql import SparkSession
import pytest
import sys

sys.path.append("../src")

from src.sparkutils import tableExists

# ----Fixture----
# Fixtures are useful when you want to run a setup function before each test function.
# The setup function is defined with the yield statement.
@pytest.fixture
def spark() -> SparkSession:
  # Create a SparkSession (the entry point to Spark functionality) on
  # the cluster in the remote Databricks workspace. Unit tests do not
  # have access to this SparkSession by default.
  return SparkSession.builder.getOrCreate()

@pytest.fixture
def setup_tables(spark):
  # Create a temporary database and table for testing
  spark.sql("CREATE DATABASE IF NOT EXISTS test_db")
  spark.sql("CREATE TABLE IF NOT EXISTS test_db.test_table (id INT, name STRING)")
  yield
  # Drop the temporary database and table after tests
  spark.sql("DROP TABLE IF EXISTS test_db.test_table")
  spark.sql("DROP DATABASE IF EXISTS test_db")

def test_tableExists_default():
  expected = True
  result = tableExists("samples.tpch", "orders")
  assert result == expected


def test_tableExists_custom(spark, setup_tables):
  assert tableExists("test_table", "test_db") is True
  assert tableExists("non_existent_table", "test_db") is False
  assert tableExists("test_table", "non_existent_db") is False


